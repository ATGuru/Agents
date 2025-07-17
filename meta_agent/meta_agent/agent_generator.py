import os
import datetime

class AgentGenerator:
    """
    Generates new agent code based on user prompts and selected tools.
    """
    def __init__(self, tool_registry, parent_dir):
        self.tool_registry = tool_registry
        self.parent_dir = parent_dir

    def generate_agent(self, prompt: str, agent_type: str = None):
        """
        Generate an agent based on the prompt and agent_type.
        If agent_type is None, use the prompt as the agent name and code.
        """
        agent_templates = {
            'code_review': self._code_review_agent,
            'doc_generator': self._doc_generator_agent,
            'data_analysis': self._data_analysis_agent,
            'web_scraper': self._web_scraper_agent,
            'task_reminder': self._task_reminder_agent,
            'git_automation': self._git_automation_agent,
            'api_monitor': self._api_monitor_agent,
            'file_organizer': self._file_organizer_agent,
            'meeting_summarizer': self._meeting_summarizer_agent,
            'security_scanner': self._security_scanner_agent,
        }
        if agent_type and agent_type in agent_templates:
            code = agent_templates[agent_type]()
            agent_name = agent_type
        else:
            code = f"""import os\n\n# Agent generated from prompt: {prompt}\n\nPARENT_DIR = '{self.parent_dir}'\n\ndef run():\n    print('Agent running with access to:', PARENT_DIR)\n    # Add tool integrations here\n\nif __name__ == '__main__':\n    run()\n"""
            agent_name = f"agent_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        agent_dir = os.path.join(self.parent_dir, agent_name)
        os.makedirs(agent_dir, exist_ok=True)
        agent_path = os.path.join(agent_dir, 'main.py')
        with open(agent_path, 'w') as f:
            f.write(code)
        return code, agent_path

    def generate_all_agents(self):
        agent_types = [
            ('code_review', 'Code Review Agent'),
            ('doc_generator', 'Documentation Generator Agent'),
            ('data_analysis', 'Data Analysis Agent'),
            ('web_scraper', 'Web Scraper Agent'),
            ('task_reminder', 'Task Reminder Agent'),
            ('git_automation', 'Git Automation Agent'),
            ('api_monitor', 'API Monitor Agent'),
            ('file_organizer', 'File Organizer Agent'),
            ('meeting_summarizer', 'Meeting Summarizer Agent'),
            ('security_scanner', 'Security Scanner Agent'),
        ]
        results = []
        for agent_type, prompt in agent_types:
            code, path = self.generate_agent(prompt, agent_type)
            results.append((agent_type, path))
        return results

    def _code_review_agent(self):
        return f"""import os\nimport subprocess\n\n# Code Review Agent\ndef run():\n    print('Running code review...')\n    result = subprocess.run(['pylint', os.path.join('{self.parent_dir}', 'YOUR_CODE_DIR')], capture_output=True, text=True)\n    print(result.stdout)\n\nif __name__ == '__main__':\n    run()\n"""

    def _doc_generator_agent(self):
        return f"""import os\n\n# Documentation Generator Agent\ndef run():\n    print('Generating documentation...')\n    # Scan files and generate docstrings or markdown\n\nif __name__ == '__main__':\n    run()\n"""

    def _data_analysis_agent(self):
        return f"""import os\nimport pandas as pd\n\n# Data Analysis Agent\ndef run():\n    print('Analyzing CSV files...')\n    for file in os.listdir('{self.parent_dir}'):\n        if file.endswith('.csv'):\n            df = pd.read_csv(os.path.join('{self.parent_dir}', file))\n            print(df.describe())\n\nif __name__ == '__main__':\n    run()\n"""

    def _web_scraper_agent(self):
        return f"""import requests\nfrom bs4 import BeautifulSoup\n\n# Web Scraper Agent\ndef run():\n    url = 'https://example.com'\n    print(f'Scraping {{url}}...')\n    r = requests.get(url)\n    soup = BeautifulSoup(r.text, 'html.parser')\n    print(soup.title.text)\n\nif __name__ == '__main__':\n    run()\n"""

    def _task_reminder_agent(self):
        return f"""import time\n\n# Task Reminder Agent\ndef run():\n    print('Task reminder running...')\n    while True:\n        print('Reminder: Check your tasks!')\n        time.sleep(3600)\n\nif __name__ == '__main__':\n    run()\n"""

    def _git_automation_agent(self):
        return f"""import os\nimport subprocess\n\n# Git Automation Agent\ndef run():\n    print('Checking for changes...')\n    subprocess.run(['git', 'add', '.'])\n    subprocess.run(['git', 'commit', '-m', 'Automated commit'])\n    subprocess.run(['git', 'push'])\n\nif __name__ == '__main__':\n    run()\n"""

    def _api_monitor_agent(self):
        return f"""import requests\n\n# API Monitor Agent\ndef run():\n    url = 'https://api.example.com/health'\n    print(f'Checking API: {{url}}')\n    r = requests.get(url)\n    print('Status:', r.status_code)\n\nif __name__ == '__main__':\n    run()\n"""

    def _file_organizer_agent(self):
        return f"""import os\nimport shutil\n\n# File Organizer Agent\ndef run():\n    print('Organizing files...')\n    for file in os.listdir('{self.parent_dir}'):\n        if file.endswith('.txt'):\n            shutil.move(os.path.join('{self.parent_dir}', file), os.path.join('{self.parent_dir}', 'text_files', file))\n\nif __name__ == '__main__':\n    run()\n"""

    def _meeting_summarizer_agent(self):
        return f"""# Meeting Summarizer Agent\ndef run():\n    print('Transcribing and summarizing meeting audio...')\n    # Integrate with speech-to-text and summarization\n\nif __name__ == '__main__':\n    run()\n"""

    def _security_scanner_agent(self):
        return f"""import os\n\n# Security Scanner Agent\ndef run():\n    print('Scanning for secrets...')\n    for root, dirs, files in os.walk('{self.parent_dir}'):\n        for file in files:\n            if file.endswith('.py'):\n                with open(os.path.join(root, file)) as f:\n                    for line in f:\n                        if 'SECRET' in line or 'PASSWORD' in line:\n                            print(f'Secret found in {{file}}: {{line.strip()}}')\n\nif __name__ == '__main__':\n    run()\n"""
