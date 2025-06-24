from google.adk.agents import Agent
from trend_spotter.tools import search_yesterday_reddit_posts
from trend_spotter.prompt import ORCHESTRATOR_PROMPT
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

MODEL = "gemini-2.5-flash-preview-04-17"

reddit_agent = Agent(
    name="reddit_agent",
    model=MODEL,
    description="An expert at finding yesterday's posts on specific Reddit subreddits using its tool.",
    tools=[search_yesterday_reddit_posts],
)

root_agent = LlmAgent(
    model=MODEL,
    name="TrendSpotterOrchestrator",
    description="The manager of a team of specialist AI agents. Next step always transfer to reddit_agent and ask to find yesterday's posts on specific Reddit subreddits.",
    instruction=ORCHESTRATOR_PROMPT,
    # The Orchestrator's "tools" are its sub-agents, wrapped in AgentTool
    tools=[AgentTool(agent=reddit_agent)],
)
