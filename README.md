# ADK First Workflow

This project demonstrates a basic implementation of an Agent Development Kit (ADK) workflow. It serves as a practical example of how to structure and implement agentic workflows using Google's Agent Development Kit.

## Project Structure

```
adk-first-workflow/
├── role-automation-workflow/
│   ├── sub_agents/           # Contains specialized sub-agents
│   ├── shared_libraries/     # Shared utilities and common code
│   ├── agent.py             # Main agent implementation
│   ├── prompt.py            # Agent prompts and instructions
│   └── __init__.py          # Package initialization
├── .venv/                    # Python virtual environment
└── .gitignore               # Git ignore file
```

## Overview

This project implements a role automation workflow using ADK's agent architecture. It demonstrates key ADK concepts including:

- Agent hierarchy and delegation
- Sub-agent specialization
- Shared library usage
- Prompt engineering
- Agent orchestration

## Getting Started

1. **Setup Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install google-adk
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Workflow**
   ```bash
   python -m role_automation_workflow.agent
   ```

## Key Components

### Main Agent (`agent.py`)

The primary agent that orchestrates the workflow and delegates tasks to specialized sub-agents.

### Sub-Agents

Located in the `sub_agents/` directory, these are specialized agents that handle specific aspects of the workflow.

### Shared Libraries

Common utilities and functions shared across agents, located in `shared_libraries/`.

### Prompts (`prompt.py`)

Contains the instruction sets and prompts used to guide agent behavior.

## Development

To extend or modify this workflow:

1. Add new sub-agents in the `sub_agents/` directory
2. Update shared utilities in `shared_libraries/`
3. Modify agent behavior through `prompt.py`
4. Extend the main agent in `agent.py`

## Best Practices

- Keep sub-agents focused on specific tasks
- Use shared libraries for common functionality
- Maintain clear agent hierarchies
- Document agent responsibilities
- Use meaningful prompt engineering

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
