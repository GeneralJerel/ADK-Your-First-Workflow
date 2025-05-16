from google.adk.agents.llm_agent import Agent

from .sub_agents import job_description_search_agent
from .sub_agents import workflow_analysis_agent
from .sub_agents import prompt_engineer_agent

#from .shared_libraries import constants

# --- 1. Define Root Agents for Each Pipeline Stage ---

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='Role Automation Workflow',
    description="",
    instruction=prompt.ROOT_PROMPT,
    sub_agents=[
        job_description_search_agent,
        workflow_analysis_agent,
        prompt_engineer_agent,
    ],
)