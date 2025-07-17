import os
import sys
import schedule
import time
from meta_agent.tool_registry import ToolRegistry
from meta_agent.agent_generator import AgentGenerator
from meta_agent.interface import ChatInterface, ScheduledTrigger

PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class MetaAgent:
    def __init__(self):
        self.tool_registry = ToolRegistry()
        self.agent_generator = AgentGenerator(self.tool_registry, PARENT_DIR)
        self.chat_interface = ChatInterface(self)
        self.scheduled_trigger = ScheduledTrigger(self)
        from meta_agent.dashboard import Dashboard
        self.dashboard = Dashboard(PARENT_DIR)
        from meta_agent.notification import notify_console
        from meta_agent.agent_templates import AgentTemplates
        self.notify = notify_console
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.agent_templates = AgentTemplates(templates_dir)

    def handle_prompt(self, prompt: str):
        print(f"[MetaAgent] Received prompt: {prompt}")
        if prompt.strip().lower() in ["dashboard", "open dashboard", "agent dashboard"]:
            self.dashboard.start()
            return
        if prompt.strip().lower() in ["create all agents", "create them all", "generate all agents"]:
            results = self.agent_generator.generate_all_agents()
            for agent_type, agent_path in results:
                self.notify(f"{agent_type} agent created at: {agent_path}")
            return results
        if prompt.strip().lower().startswith("create agent from template"):
            # Usage: create agent from template <template_name> <agent_name>
            parts = prompt.strip().split()
            if len(parts) >= 6:
                template_name = parts[4]
                agent_name = parts[5]
                agent_path = self.agent_templates.create_agent_from_template(template_name, agent_name, PARENT_DIR)
                self.notify(f"Agent '{agent_name}' created from template '{template_name}' at {agent_path}")
                return agent_path
            else:
                self.notify("Usage: create agent from template <template_name> <agent_name>")
                return
        else:
            agent_code, agent_path = self.agent_generator.generate_agent(prompt)
            self.notify(f"Agent created at: {agent_path}")
            return agent_path

    def run(self):
        self.chat_interface.start()
        self.scheduled_trigger.start()

if __name__ == "__main__":
    meta_agent = MetaAgent()
    meta_agent.run()
