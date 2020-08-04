import requests
from bs4 import BeautifulSoup
import csv
soup_list = []
for i in range(1,102,10):
    base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    start_num = i
    end_url = '&refresh_start=0'

    my_url = base_url + str(start_num) + end_url

    respnse = requests.get(my_url)
    soup = BeautifulSoup(respnse.text, 'html.parser')

    
    # news_section2 = soup.select_one('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01]')
    soup_list.append(soup)

new_list =[]
for soup in soup_list:
    news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li') 
    for news in news_section:
        title = news.select_one('dl > dt > a')
        # print(title['href'], '\n')
        # print(title.text, '\n')
        new ={
            'title' : title['title'],'link' : title['href']
        }
        new_list.append(new)

with open('technology.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['title', 'link']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    # 1 Row 쓸 때
    for new in new_list:
        writer.writerow(new)




