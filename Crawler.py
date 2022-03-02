import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/quotes/tag/god'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(2) > div.quoteDetails > div.quoteText')
    print(title.get_text())
else : 
    print(response.status_code)

