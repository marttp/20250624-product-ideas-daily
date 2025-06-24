from trend_spotter.prompt import ORCHESTRATOR_PROMPT, SOLUTION_DESIGN_TEAM_PROMPT
from google.adk.agents import LlmAgent, SequentialAgent
from trend_spotter.config import MODEL
from trend_spotter.sub_agents import product_manager_agent
from trend_spotter.sub_agents.reddit_agent import reddit_agent
from trend_spotter.sub_agents.solution_architect_agent import solution_architect_agent


solution_design_group = SequentialAgent(
    name="solution_design_agent",
    description="An expert at designing solutions for product ideas through sequential analysis.",
    instruction=SOLUTION_DESIGN_TEAM_PROMPT,
    sub_agents=[product_manager_agent, solution_architect_agent],
)

entrepreneur_workshop_group = SequentialAgent(
    name="entrepreneur_workshop_group",
    description="A comprehensive product discovery and design workflow that combines market research with solution development.",
    instruction="Execute a sequential workflow: first gather market insights from Reddit conversations, then analyze and enhance the most promising opportunities through collaborative design analysis.",
    sub_agents=[reddit_agent, solution_design_group],
)

root_agent = LlmAgent(
    model=MODEL,
    name="TrendSpotterOrchestrator",
    description="The manager of a team of specialist AI agents. Next step always transfer to reddit_agent and ask to find yesterday's posts on specific Reddit subreddits.",
    instruction=ORCHESTRATOR_PROMPT,
    sub_agents=[entrepreneur_workshop_group],
)
