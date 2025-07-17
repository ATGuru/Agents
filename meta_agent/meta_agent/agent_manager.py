import os
import subprocess
import threading
import time
from datetime import datetime

class AgentManager:
    """
    Manages agents: start, stop, status, logs, and scheduling.
    """
    def __init__(self, agents_root):
        self.agents_root = agents_root
        self.running_agents = {}
        self.agent_logs = {}
        self.agent_status = {}

    def list_agents(self):
        return [d for d in os.listdir(self.agents_root) if os.path.isdir(os.path.join(self.agents_root, d))]

    def start_agent(self, agent_name):
        agent_path = os.path.join(self.agents_root, agent_name, 'main.py')
        if not os.path.exists(agent_path):
            print(f"Agent {agent_name} not found.")
            return
        log_file = os.path.join(self.agents_root, agent_name, 'agent.log')
        def run_agent():
            with open(log_file, 'a') as log:
                process = subprocess.Popen(['python', agent_path], stdout=log, stderr=log)
                self.running_agents[agent_name] = process
                self.agent_status[agent_name] = {'status': 'running', 'last_run': datetime.now()}
                process.wait()
                self.agent_status[agent_name]['status'] = 'stopped'
        t = threading.Thread(target=run_agent, daemon=True)
        t.start()
        print(f"Started agent {agent_name}.")

    def stop_agent(self, agent_name):
        process = self.running_agents.get(agent_name)
        if process:
            process.terminate()
            self.agent_status[agent_name]['status'] = 'stopped'
            print(f"Stopped agent {agent_name}.")
        else:
            print(f"Agent {agent_name} is not running.")

    def agent_log(self, agent_name):
        log_file = os.path.join(self.agents_root, agent_name, 'agent.log')
        if os.path.exists(log_file):
            with open(log_file) as f:
                return f.read()
        return "No log found."

    def agent_info(self, agent_name):
        return self.agent_status.get(agent_name, {'status': 'unknown'})
