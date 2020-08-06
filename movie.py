import requests
from bs4 import BeautifulSoup

my_url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(my_url)
soup = BeautifulSoup(response.text, 'html.parser')

movies_section = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
movie_list =[]
for movie in movies_section:
    title = movie.select_one('dl > dt > a')
    movie_info ={
            'title' : title.text,'code' : title['href'].split('=')[1]
        }
    movie_list.append(movie_info)
    # movie_list[title.text] = title['href'].split('=')[1]

# iframe 때문에안됨 
# for movie in movie_list:
#     movie_code = movie['code']
#     review_url = f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}'
#     review_response = requests.get(review_url)
#     review_soup2 = BeautifulSoup(review_response.text, 'html.parser')
#     review_section = soup.select('body > div > div > div.score_result > ul > li')


review_section_list=[]
for movie in movie_list:
    movie_code = movie['code']
    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )
    # headers = {
    # 'authority': 'movie.naver.com',
    # 'upgrade-insecure-requests': '1',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-dest': 'iframe',
    # 'referer': f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}',
    # 'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,ja;q=0.4',
    # }
    
    review_response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)
    review_soup2 = BeautifulSoup(review_response.text, 'html.parser')
    review_section = review_soup2.select('body > div > div > div.score_result > ul > li')
    review_section_list.append(review_section)

for review in review_section_list:
    j=0
    for i in review:
        title = i.select_one(f'div.score_reple > p > span[id=_filtered_ment_{j}]')
        if title:
            print(title.text)
        j += 1
    
    
