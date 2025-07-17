import os
import importlib

class ToolAutoDiscovery:
    """
    Scans the workspace for new tool modules and registers them.
    """
    def __init__(self, tools_dir):
        self.tools_dir = tools_dir
        self.discovered_tools = {}

    def scan_tools(self):
        for fname in os.listdir(self.tools_dir):
            if fname.endswith('.py') and fname != '__init__.py':
                tool_name = fname[:-3]
                if tool_name not in self.discovered_tools:
                    module = importlib.import_module(f"meta_agent.tools.{tool_name}")
                    self.discovered_tools[tool_name] = module
        return list(self.discovered_tools.keys())
