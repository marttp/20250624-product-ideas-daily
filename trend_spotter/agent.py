from trend_spotter.prompt import ORCHESTRATOR_PROMPT
from google.adk.agents import LlmAgent, SequentialAgent
from trend_spotter.config import MODEL
from trend_spotter.sub_agents.reddit_agent import reddit_agent
from trend_spotter.sub_agents.workshop_group import product_manager_agent, solution_architect_agent


solution_design_group = SequentialAgent(
    name="solution_design_agent",
    description="An expert at designing solutions for product ideas through sequential analysis.",
    sub_agents=[product_manager_agent, solution_architect_agent],
)

entrepreneur_workshop_group = SequentialAgent(
    name="entrepreneur_workshop_group",
    description="A comprehensive product discovery and design workflow that combines market research with solution development.",
    sub_agents=[reddit_agent, solution_design_group],
)

root_agent = LlmAgent(
    model=MODEL,
    name="TrendSpotterOrchestrator",
    description="The manager of a team of specialist AI agents. Next step always transfer to reddit_agent and ask to find yesterday's posts on specific Reddit subreddits.",
    instruction=ORCHESTRATOR_PROMPT,
    sub_agents=[entrepreneur_workshop_group],
)
