from google.adk.agents.llm_agent import Agent
# search

from . import prompt

job_description_search_agent = Agent(
    model=constants.MODEL,
    name="job_description_search_agent",
    description="A helpful agent to find job descriptions",
    instruction=prompt.JOB_DESCRIPTION_SEARCH_AGENT_PROMPT,
    tools=[
        
    ],
)