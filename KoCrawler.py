# saramro 한국어 명언 사이트에서 크롤링

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

#data = pd.read_csv('./dataset.csv')

for page in range(1, 1026):
    url = 'https://saramro.com/quotes?page=' + str(page)

    response = requests.get(url)
    print(page)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find('tbody')
        tagA = data.findAll('a')
        hrefs = []
        for i in tagA:
            hrefs.append(i.attrs['href'])
        
        for i in hrefs:
            res = requests.get(i)
            if res.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # 한 페이지내의 링크들에서 제목과, 태그, 본문만 추출하여 저장하면 끝
                

            else : print(response.status_code)
    
    else : 
        print(response.status_code)

    


data.to_csv('dataset.csv', index=False)
