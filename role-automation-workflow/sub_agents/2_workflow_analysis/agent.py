from google.adk.agents.llm_agent import Agent


from . import prompt

workflow_analysis_agent = Agent(
    model=constants.MODEL,
    name="workflow_analysis_agent",
    description="A helpful agent to analyze workflows",
    instruction=prompt.WORKFLOW_ANALYSIS_AGENT_PROMPT,
)

