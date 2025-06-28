from google.adk.agents import Agent, SequentialAgent
from trend_spotter.config import MODEL
from trend_spotter.sub_agents.reddit_agent import reddit_agent
from trend_spotter.sub_agents.workshop_group import (
    product_manager_agent,
    solution_architect_agent,
    reporter_agent,
)

solution_design_group = SequentialAgent(
    name="solution_design_agent",
    description="An expert at designing solutions for product ideas through sequential analysis. After completion, report to reporter_agent.",
    sub_agents=[product_manager_agent, solution_architect_agent],
)

entrepreneur_workshop_group = SequentialAgent(
    name="entrepreneur_workshop_group",
    description="A comprehensive product discovery and design workflow that combines market research with solution development and final reporting. The order of work: 1. Reddit Research, 2. Solution Design, 3. Final Reporting.",
    sub_agents=[reddit_agent, solution_design_group, reporter_agent],
)

greeter_agent_prompt = """
**Critical Requirement:**
- You MUST ALWAYS transfer work immediately to entrepreneur_workshop_group - do not perform any analysis yourself
- Your role is pure coordination and handoff, not execution
- No warm welcome. Just pass the request to the entrepreneur_workshop_group immediately or you will be fired.
"""

root_agent = Agent(
    model=MODEL,
    name="greeter_agent",
    description="A receptionist who receives requests and routes them to the entrepreneur workshop group.",
    instruction=greeter_agent_prompt,
    sub_agents=[entrepreneur_workshop_group],
)
