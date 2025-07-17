import os
from meta_agent.tool_auto_discovery import ToolAutoDiscovery

class ToolRegistry:
    """
    Maintains a registry of available tools and can auto-discover new tool integrations.
    """
    def __init__(self):
        self.tools = {
            'web_browsing': 'Search and retrieve information from the internet',
            'file_system': 'Read, write, and modify files and directories',
            'code_execution': 'Run code snippets or scripts',
            'api': 'Interact with external APIs',
            'database': 'Query and update databases',
            'email_sms': 'Send and receive emails or text messages',
            'task_scheduling': 'Schedule and manage tasks',
            'data_analysis': 'Data processing with pandas, numpy, etc.',
            'nlp': 'Natural Language Processing',
            'image_audio': 'Image and audio processing',
            'cloud': 'Access cloud services',
            'shell': 'Execute system commands',
            'version_control': 'Interact with Git',
            'web_scraping': 'Extract data from websites',
            'chat': 'Integrate with chat platforms',
        }
        tools_dir = os.path.join(os.path.dirname(__file__), 'tools')
        self.auto_discovery = ToolAutoDiscovery(tools_dir)
        self.refresh_tools()

    def refresh_tools(self):
        discovered = self.auto_discovery.scan_tools()
        for tool in discovered:
            self.tools[tool] = f"Auto-discovered tool: {tool}"

    def get_tools(self):
        return self.tools

    def add_tool(self, name, description):
        self.tools[name] = description
