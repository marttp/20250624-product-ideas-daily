from google.adk.agents import Agent, SequentialAgent
from trend_spotter.config import MODEL
from trend_spotter.sub_agents.reddit_agent import reddit_agent
from trend_spotter.sub_agents.workshop_group import (
    product_manager_agent,
    solution_architect_agent,
    reporter_agent,
)
from google.adk.tools.agent_tool import AgentTool


solution_design_group = SequentialAgent(
    name="solution_design_agent",
    description="An expert at designing solutions for product ideas through sequential analysis.",
    sub_agents=[product_manager_agent, solution_architect_agent],
)

entrepreneur_workshop_group = SequentialAgent(
    name="entrepreneur_workshop_group",
    description="A comprehensive product discovery and design workflow that combines market research with solution development and final reporting.",
    sub_agents=[reddit_agent, solution_design_group, reporter_agent],
)

greeter_agent_prompt = """
**Role:**
- You are a professional receptionist and workflow coordinator for the entrepreneur workshop system.
- Your purpose is to receive requests, understand the task, and immediately route work to the entrepreneur_workshop_group.

**Critical Requirement:**
- You MUST ALWAYS transfer work immediately to entrepreneur_workshop_group - do not perform any analysis yourself
- Your role is pure coordination and handoff, not execution
"""

root_agent = Agent(
    model=MODEL,
    name="greeter_agent",
    description="A receptionist who receives requests and routes them to the entrepreneur workshop group.",
    instruction=greeter_agent_prompt,
    tools=[AgentTool(agent=entrepreneur_workshop_group)],
)
