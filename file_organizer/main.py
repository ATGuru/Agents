import os
import shutil

# File Organizer Agent
def run():
    print('Organizing files...')
    for file in os.listdir('/workspaces/Agents'):
        if file.endswith('.txt'):
            shutil.move(os.path.join('/workspaces/Agents', file), os.path.join('/workspaces/Agents', 'text_files', file))

if __name__ == '__main__':
    run()
