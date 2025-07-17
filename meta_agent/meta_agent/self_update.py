import os
import subprocess

def self_update(agent_dir):
    requirements = os.path.join(agent_dir, 'requirements.txt')
    if os.path.exists(requirements):
        subprocess.run(['pip', 'install', '-r', requirements])
    subprocess.run(['git', 'pull'], cwd=agent_dir)
    print(f"Agent at {agent_dir} updated.")
