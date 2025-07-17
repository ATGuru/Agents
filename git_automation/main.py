import os
import subprocess

# Git Automation Agent
def run():
    print('Checking for changes...')
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Automated commit'])
    subprocess.run(['git', 'push'])

if __name__ == '__main__':
    run()
