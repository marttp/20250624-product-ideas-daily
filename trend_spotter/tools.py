import praw
import logging
import os
from datetime import datetime, timedelta
from google.adk.tools.tool_context import ToolContext
from google.cloud import firestore


def search_yesterday_reddit_posts(
    subreddit_names: list[str] = [
        "Entrepreneur",
        "startups",
        "smallbusiness",
        "business",
        "freelance",
        "unpopularopinion",
    ],
    limit_per_subreddit: int = 5,
) -> str:
    """
    Searches a list of subreddits for posts from yesterday and returns their titles and URLs.

    Args:
        subreddit_names: A list of subreddit names to search (e.g., ["LocalLLaMA", "MachineLearning"]).
        limit_per_subreddit: The number of top posts to retrieve from each subreddit.

    Returns:
        A string containing formatted post information.
    """
    try:
        print(
            f"\n🔎 Searching Reddit for yesterday's posts in: {', '.join(subreddit_names)}..."
        )
        REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
        REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
        REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
            read_only=True,
        )

        yesterday = datetime.now() - timedelta(days=1)
        yesterday_start = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
        yesterday_end = yesterday.replace(
            hour=23, minute=59, second=59, microsecond=999999
        )

        all_posts = []
        for sub_name in subreddit_names:
            print(f"  - Fetching from r/{sub_name}...")
            subreddit = reddit.subreddit(sub_name)
            for post in subreddit.new(limit=50):
                post_time = datetime.fromtimestamp(post.created_utc)
                if yesterday_start <= post_time <= yesterday_end:
                    all_posts.append(
                        f"Title: {post.title}\nLink: {post.url}\nScore: {post.score}"
                    )

        if not all_posts:
            return "No posts from yesterday found meeting the criteria in the specified subreddits."

        all_posts.sort(key=lambda x: int(x.split("Score: ")[1]), reverse=True)
        all_posts = all_posts[: limit_per_subreddit * len(subreddit_names)]

        print(
            f"✅ Reddit search complete. Found {len(all_posts)} qualifying posts from yesterday."
        )
        return "\n---\n".join(all_posts)

    except Exception as e:
        return f"Error searching Reddit for yesterday's posts: {e}"


def append_to_state(
    tool_context: ToolContext, field: str, response: str
) -> dict[str, str]:
    """Append new output to an existing state key.

    Args:
        field (str): a field name to append to
        response (str): a string to append to the field

    Returns:
        dict[str, str]: {"status": "success"}
    """
    existing_state = tool_context.state.get(field, [])
    tool_context.state[field] = existing_state + [response]
    logging.info(f"[Added to {field}] {response}")
    return {"status": "success"}


def set_firestore_data(data: dict) -> dict[str, str]:
    """Set data to Firestore collection 'product_ideas' with document ID as today's date.

    Args:
        data (dict): Dictionary containing the data to store in Firestore

    Returns:
        dict[str, str]: {"status": "success"} or {"status": "error", "message": "error details"}
    """
    try:
        # Initialize Firestore client
        db = firestore.Client()
        # Set data to product_ideas collection with today's date as document ID
        doc_ref = db.collection("product_ideas").document("today")
        doc_ref.set(data)
        logging.info(f"Successfully set data to Firestore: product_ideas/today")
        return {"status": "success"}
    except Exception as e:
        error_msg = f"Error setting data to Firestore: {str(e)}"
        logging.error(error_msg)
        return {"status": "error", "message": error_msg}
