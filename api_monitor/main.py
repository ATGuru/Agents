import requests

# API Monitor Agent
def run():
    url = 'https://api.example.com/health'
    print(f'Checking API: {url}')
    r = requests.get(url)
    print('Status:', r.status_code)

if __name__ == '__main__':
    run()
