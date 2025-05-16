# ADK First Workflow

This project demonstrates a basic implementation of an Agent Development Kit (ADK) workflow for role automation. It serves as a practical example of how to structure and implement agentic workflows using Google's Agent Development Kit.

## Project Structure

```
adk-first-workflow/
├── role-automation-workflow/
│   ├── sub_agents/           # Contains specialized sub-agents
│   │   ├── __init__.py      # Exports sub-agents
│   │   ├── agent.py         # Sub-agent implementations
│   │   └── prompt.py        # Sub-agent prompts
│   ├── agent.py            # Main agent implementation
│   ├── prompt.py           # Agent prompts and instructions
│   └── __init__.py         # Package initialization
├── .venv/                   # Python virtual environment
└── .gitignore              # Git ignore file
```

## Overview

This project implements a role automation workflow using ADK's agent architecture. The workflow consists of three specialized sub-agents that work together in sequence:

1. **Job Description Search Agent**: Analyzes and extracts key information from job descriptions
2. **Workflow Analysis Agent**: Processes the extracted information to identify workflows
3. **Prompt Engineer Agent**: Creates optimized prompts based on the workflow analysis

## Prerequisites

- Python 3.8+
- Google ADK (`pip install google-adk`)
- Gemini API Key (from Google AI Studio)

## Getting Started

1. **Setup Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install google-adk
   ```

2. **Configure API Keys**
   Create a `.env` file in the project root:

   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

3. **Run the Workflow**

   ```bash
   # Using ADK CLI
   adk run role-automation-workflow

   # Or using ADK Web UI
   adk web
   ```

## Key Components

### Main Agent (`agent.py`)

The primary agent that orchestrates the workflow using ADK's `SequentialAgent` class to ensure ordered execution of sub-agents.

### Sub-Agents

Located in the `sub_agents/` directory, each specialized agent handles a specific aspect of the workflow:

- `job_description_search_agent`: Extracts and analyzes job descriptions
- `workflow_analysis_agent`: Processes workflow information
- `prompt_engineer_agent`: Creates optimized prompts

### Prompts (`prompt.py`)

Contains the instruction sets and prompts used to guide agent behavior.

## Development

To extend or modify this workflow:

1. Add new sub-agents in the `sub_agents/` directory
2. Modify agent behavior through `prompt.py`
3. Extend the main agent in `agent.py`

## Best Practices

- Keep sub-agents focused on specific tasks
- Maintain clear agent hierarchies
- Document agent responsibilities
- Use meaningful prompt engineering
- Implement proper error handling
- Use session state for maintaining context

## Advanced Features

The project can be extended with:

- Persistent session storage
- Advanced callbacks for model and tool interactions
- Error handling and retry logic
- Streaming UI integration
- Custom tool implementations

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
