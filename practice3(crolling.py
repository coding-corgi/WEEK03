import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser') #텍스트 받아오고 html로 파싱한다.


#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a




#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img  순위


movie_list = soup.select("#old_content > table > tbody > tr") #셀렉트를 하면 리스트에 들어가게ㅐ됨



for movie in movie_list:
    ranking = movie.select_one("td:nth-child(1) > img")
    title = movie.select_one("td.title > div > a")
    point = movie.select_one("td.point")

    if title:
        print(ranking['alt'], title.text, point.text)





