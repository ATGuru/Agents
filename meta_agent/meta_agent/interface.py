import threading
import schedule
import time

class ChatInterface:
    def __init__(self, meta_agent):
        self.meta_agent = meta_agent

    def start(self):
        print("[ChatInterface] Type your prompt (or 'exit' to quit):")
        while True:
            prompt = input('> ')
            if prompt.lower() == 'exit':
                break
            self.meta_agent.handle_prompt(prompt)

class ScheduledTrigger:
    def __init__(self, meta_agent):
        self.meta_agent = meta_agent
        self.thread = threading.Thread(target=self.run_schedule, daemon=True)

    def start(self):
        # Example: schedule a prompt every day at 9am
        schedule.every().day.at("09:00").do(self.trigger)
        self.thread.start()

    def trigger(self):
        prompt = "Scheduled agent creation prompt."
        self.meta_agent.handle_prompt(prompt)

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
