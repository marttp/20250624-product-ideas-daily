from google.adk.agents import Agent
from trend_spotter.tools import search_yesterday_reddit_posts
from trend_spotter.config import MODEL

reddit_agent = Agent(
    name="reddit_agent",
    model=MODEL,
    description="An expert at finding yesterday's posts on specific Reddit subreddits using its tool.",
    tools=[search_yesterday_reddit_posts],
)