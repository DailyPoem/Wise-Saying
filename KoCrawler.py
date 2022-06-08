# saramro 한국어 명언 사이트에서 크롤링

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


for page in range(801, 1026):
    url = 'https://saramro.com/quotes?page=' + str(page)

    response = requests.get(url)
    print(page)
    dataset = pd.read_csv('./KO_dataset.csv')
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find('tbody')
        tagA = data.findAll('a')
        hrefs = []
        for i in tagA:
            hrefs.append(i.attrs['href'])
        #print('href : ' + str(len(hrefs)))
        for i in hrefs:
            res = requests.get(i)
            if res.status_code == 200:
                #print(i)
                html2 = res.text
                soup2 = BeautifulSoup(html2, 'html.parser')
                # 한 페이지내의 링크들에서 제목과, 태그, 본문만 추출하여 저장하면 끝
                title = soup2.find("span",{"class": "bo_v_tit"})
                tag = ((str(title.text).split('-')[0]).replace('\n', '')).replace(' ', '')
                content = soup2.find("div",{"id": "bo_v_con"}).find_all(text=True)
                dataset = dataset.append({'author': content[1],'content':content[0],'tag':tag}, ignore_index=True)
            else : print(response.status_code)
    
    else : 
        print(response.status_code)
    for i in dataset.columns:
        if i not in ['author', 'content', 'tag']:
            dataset = dataset.drop(i, axis=1)
    dataset.to_csv('KO_dataset.csv')
