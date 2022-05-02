# saramro 한국어 명언 사이트에서 크롤링

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

#data = pd.read_csv('./dataset.csv')


TAG = ['love', 'life', 'inspirational', 'humor', 'philosophy', 'god', 'truth', 'wisdom', 'poetry', 'romance', 'death', 'happiness', 'hope', 'faith', 'quotes', 'life-lessons', 'writing', 'motivational', 'religion', 'success', 'time', 'knowledge', 'science']
t = 'science'

url = 'https://saramro.com/quotes'

response = requests.get(url)
print(response.text)


'''
for page in range(1, 101):
    url = 'https://www.goodreads.com/quotes/tag/' + t + '?page=' + str(page)

    response = requests.get(url)
    print(page)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for count in range(30):
            title = soup.select('.quoteText')[count].get_text()

            txt = title.split('\n')

            data = data.append({'author' : txt[4], 'content' : txt[1], 'tag' : t}, ignore_index=True)
    
    else : 
        print(response.status_code)


data.to_csv('dataset.csv', index=False)
'''