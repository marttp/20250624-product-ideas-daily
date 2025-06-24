from trend_spotter.prompt import ORCHESTRATOR_PROMPT
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from trend_spotter.config import MODEL
from trend_spotter.sub_agents.reddit_agent import reddit_agent
from trend_spotter.sub_agents.google_search_agent import google_search_agent
from trend_spotter.sub_agents.solution_architect_agent import solution_architect_agent

root_agent = LlmAgent(
    model=MODEL,
    name="TrendSpotterOrchestrator",
    description="The manager of a team of specialist AI agents. Next step always transfer to reddit_agent and ask to find yesterday's posts on specific Reddit subreddits.",
    instruction=ORCHESTRATOR_PROMPT,
    # The Orchestrator's "tools" are its sub-agents, wrapped in AgentTool
    tools=[AgentTool(agent=reddit_agent), AgentTool(agent=google_search_agent), AgentTool(agent=solution_architect_agent)],
)
