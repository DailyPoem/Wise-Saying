# 크롤링 코드 테스트

from cgitb import text
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('KO_dataset.csv', encoding='utf-8')

url = "https://saramro.com/quotes/16335"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.find("span",{"class": "bo_v_tit"})
tag = ((str(title.text).split('-')[0]).replace('\n', '')).replace(' ', '')
content = soup.find("div",{"id": "bo_v_con"}).find_all(text=True)
print(tag)
print(content[0])
print(content[1])

df.append({'author': content[1],'content':content[0],'tag':tag}, ignore_index=True)
df.to_csv('KO_dataset.csv')


'''
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
'''