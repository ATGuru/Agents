import schedule
import threading
import time
from meta_agent.agent_manager import AgentManager

class AgentScheduler:
    def __init__(self, agents_root):
        self.agent_manager = AgentManager(agents_root)
        self.schedules = {}
        self.thread = threading.Thread(target=self.run, daemon=True)

    def schedule_agent(self, agent_name, cron_time):
        def job():
            self.agent_manager.start_agent(agent_name)
        schedule.every().day.at(cron_time).do(job)
        self.schedules[agent_name] = cron_time
        print(f"Scheduled {agent_name} at {cron_time}")

    def start(self):
        self.thread.start()

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
