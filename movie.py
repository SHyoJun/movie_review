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
print(movie_list)
# movie_name = input()
# print(movie_list['반도'])

# review_url = f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_list["반도"]}'
# soup2 = BeautifulSoup(response.text, 'html.parser')
# review_section = soup.select('body > div > div > div.score_result > ul > li')
# i=1
# for review in review_section:
#     # conent = review.select_one('dvi.score_reple > p > span.id._filtered_ment_0 > span.id._unfold_ment0 > a')
#     conent = review.select_one(f'dvi.score_reple > p > span[id=_filtered_ment_{i}]')
#     i+=1
#     print(conent.text)