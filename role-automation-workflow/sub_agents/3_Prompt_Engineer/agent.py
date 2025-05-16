from google.adk.agents.llm_agent import Agent

from . import prompt

prompt_engineer_agent = Agent(
    model=constants.MODEL,
    name="prompt_engineer_agent",
    description="A helpful agent to engineer prompts",
    instruction=prompt.PROMPT_ENGINEER_AGENT_PROMPT,
)


