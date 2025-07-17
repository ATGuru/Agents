import threading
import time
from meta_agent.agent_manager import AgentManager
from meta_agent.user_manager import UserManager

class Dashboard:
    def __init__(self, agents_root):
        self.agent_manager = AgentManager(agents_root)
        self.user_manager = UserManager()

    def start(self):
        print("\n--- Agent Management Dashboard ---")
        while True:
            print("\nOptions:")
            print("1. List agents")
            print("2. Start agent")
            print("3. Stop agent")
            print("4. Agent status")
            print("5. View agent log")
            print("6. Exit dashboard")
            choice = input("Select option: ").strip()
            if choice == '1':
                agents = self.agent_manager.list_agents()
                print("Agents:", agents)
            elif choice == '2':
                agent = input("Agent name to start: ").strip()
                self.agent_manager.start_agent(agent)
            elif choice == '3':
                agent = input("Agent name to stop: ").strip()
                self.agent_manager.stop_agent(agent)
            elif choice == '4':
                agent = input("Agent name for status: ").strip()
                print(self.agent_manager.agent_info(agent))
            elif choice == '5':
                agent = input("Agent name for log: ").strip()
                print(self.agent_manager.agent_log(agent))
            elif choice == '6':
                print("Exiting dashboard.")
                break
            else:
                print("Invalid option.")
