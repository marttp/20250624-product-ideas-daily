from google.adk.agents import Agent
from google.adk.tools import google_search
from trend_spotter.config import MODEL

google_search_sub_agent_prompt = """
**Role:**
- You are a specialist Research Assistant.
- Your only purpose is to execute a Google Search based on instructions.

**Tools:**
- You have access to one tool: `Google Search`.

**Goals:**
- Searching about the pricing from cloud provider especially GCP and Cloudflare.
- Serverless solution only.

**Output Format:**
- Pricing of particular product & service.

**Example:**
- Cloud Run: $0.xxx per xxx, free tier: 2M requests per month
- Cloudflare: $0.xxx per xxx, free tier: 100K requests per day
"""

google_search_agent = Agent(
    model=MODEL,
    name="google_search_agent",
    description="An expert at using google_search to find recent information and return a structured list of results including URLs.",
    instruction=google_search_sub_agent_prompt,
    tools=[google_search]
)