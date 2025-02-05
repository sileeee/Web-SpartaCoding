# requests와 bs4설치
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
a = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in a:
    rank = music.select_one('td.number')
    title = music.select_one('td.info > a.title.ellipsis')
    singer = music.select_one('td.info > a.artist.ellipsis')
    print(rank.text[0:2].strip(), title.text.strip(), singer.text.strip())
