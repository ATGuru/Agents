import os
import shutil

class AgentTemplates:
    """
    Provides reusable agent templates for quick agent creation.
    """
    def __init__(self, templates_dir):
        self.templates_dir = templates_dir
        if not os.path.exists(templates_dir):
            os.makedirs(templates_dir)

    def list_templates(self):
        return [f[:-3] for f in os.listdir(self.templates_dir) if f.endswith('.py')]

    def create_agent_from_template(self, template_name, agent_name, dest_dir):
        src = os.path.join(self.templates_dir, template_name + '.py')
        dst_dir = os.path.join(dest_dir, agent_name)
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, 'main.py')
        shutil.copyfile(src, dst)
        return dst
