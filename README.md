# Meta-Agent: Autonomous Agent Generator

Meta-Agent is an advanced AI system that can generate, manage, and operate other AI agents based on user prompts. It provides a chatbot UI, dashboard, API, and extensible toolset for building and orchestrating agents for a wide range of automation and intelligence tasks.

## Features

- **Web-based Chatbot UI**: Interact with the Meta-Agent via a modern web chat interface.
- **Agent Management Dashboard**: Start, stop, monitor, and view logs for all agents.
- **Agent Status Monitoring**: Track running agents, last run times, and errors.
- **Custom Scheduling**: Schedule agents to run at specific times.
- **Notification System**: Console notifications on agent events (extensible to email/Slack).
- **Agent Templates**: Quickly create new agents from reusable templates.
- **Tool Auto-Discovery**: Automatically detect and register new tools.
- **Interactive Agent Logs**: View real-time logs for each agent.
- **Role-Based Access Control**: Simple admin/user management for agent operations.
- **API for Agent Control**: HTTP API for programmatic agent management.
- **Self-Updating Agents**: Agents can update their own code and dependencies.

## Built-in Agent Types

The Meta-Agent can generate the following specialized agents:

1. **Code Review Agent**: Reviews code for bugs, style, and improvements.
2. **Documentation Generator Agent**: Generates or updates documentation from code.
3. **Data Analysis Agent**: Analyzes CSV files and provides summary statistics.
4. **Web Scraper Agent**: Scrapes data from specified websites.
5. **Task Reminder Agent**: Sends periodic reminders for tasks.
6. **Git Automation Agent**: Automates git add, commit, and push operations.
7. **API Monitor Agent**: Checks the health/status of APIs.
8. **File Organizer Agent**: Organizes files by type or rule.
9. **Meeting Summarizer Agent**: Transcribes and summarizes meeting audio.
10. **Security Scanner Agent**: Scans code for secrets and vulnerabilities.

## Agent Templates

- **hello_world**: Simple agent that prints a greeting.
- **file_lister**: Lists files in the current directory.

## Getting Started

1. Install dependencies: `pip install -r meta_agent/requirements.txt`
2. Start the chatbot UI: `python meta_agent/web_chat.py` and open [http://localhost:5002/](http://localhost:5002/)
3. Use the dashboard by typing `dashboard` in the chat, or manage agents via the API.

## Extending

- Add new agent templates in `meta_agent/templates/`.
- Add new tools in `meta_agent/tools/` for auto-discovery.
- Extend notifications in `meta_agent/notification.py`.

---
