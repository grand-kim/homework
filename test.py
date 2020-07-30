import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기

sports = soup.select('#regularTeamRecordList_table > tr')

# movies (tr들) 의 반복문을 돌리기
for sport in sports:
    # movie 안에 a 가 있으면,
    rank = sport.select_one('th > strong').text
    name = sport.select_one('td.tm > div > span').text
    print(rank, name)
#    if a_tag is not None:
#        rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
#        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
#        star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
#        print(rank, title, star)

