import requests
from bs4 import BeautifulSoup

# Web Scraper Agent
def run():
    url = 'https://example.com'
    print(f'Scraping {url}...')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title.text)

if __name__ == '__main__':
    run()
