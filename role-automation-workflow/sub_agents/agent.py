from google.adk.agents.llm_agent import Agent
# search

from . import prompt

# --- 1. Define Sub-Agents for Each Pipeline Stage ---

job_description_search_agent = Agent(
    model=constants.MODEL,
    name="job_description_search_agent",
    description="A helpful agent to find job descriptions",
    instruction=prompt.JOB_DESCRIPTION_SEARCH_AGENT_PROMPT,
    tools=[
        
    ],
)

workflow_analysis_agent = Agent(
    model=constants.MODEL,
    name="workflow_analysis_agent",
    description="A helpful agent to analyze workflows",
    instruction=prompt.WORKFLOW_ANALYSIS_AGENT_PROMPT,
)


prompt_engineer_agent = Agent(
    model=constants.MODEL,
    name="prompt_engineer_agent",
    description="A helpful agent to engineer prompts",
    instruction=prompt.PROMPT_ENGINEER_AGENT_PROMPT,
)
