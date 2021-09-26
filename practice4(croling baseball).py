import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser') #텍스트 받아오고 html로 파싱한다.






baseball_list = soup.select("#regularTeamRecordList_table > tr") #셀렉트를 하면 리스트에 들어가게ㅐ됨

#regularTeamRecordList_table > tr:nth-child(1) > th > strong 순위
#regularTeamRecordList_table > tr:nth-child(1) > td.tm > div > img
#regularTeamRecordList_table > tr:nth-child(6) > td.tm > div > team_SK


#regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(7) > strong 승률
for baseball in baseball_list:


    rank =baseball.select_one("th > strong")
    team =baseball.select_one("td.tm > div")
    win_lose = baseball.select_one("td:nth-child(7) > strong")
#

    if float(win_lose.text) >0.5:
        print(rank.text,team.span.text,win_lose.text)

