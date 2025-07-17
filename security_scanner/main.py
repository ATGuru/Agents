import os

# Security Scanner Agent
def run():
    print('Scanning for secrets...')
    for root, dirs, files in os.walk('/workspaces/Agents'):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        if 'SECRET' in line or 'PASSWORD' in line:
                            print(f'Secret found in {file}: {line.strip()}')

if __name__ == '__main__':
    run()
