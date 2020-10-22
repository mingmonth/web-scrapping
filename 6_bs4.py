import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a)   # soup 객체에서 처음 발견되는 a element 출력
#print(soup.a.attrs) # a element 의 속성 정보를 출력
#print(soup.a["href"])   # a element 의 href 속성 값 정보를 출력

#print(soup.find("a", attrs={"class":"Nbtn_upload"}))    # class="Nbtn_upload" 인 a element 를 찾아줘

rank1 = soup.find("li", attrs={"class": "rank01"})
#print(rank1.a)
#print(rank1.a.get_text())
#print(rank1.next_sibling)   # 태그 사이에 개행 정보가 있어서 바로 표시가 안될 수 있음
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling # 해당 엘리먼트 기준으로 다음 다음
#rank2 = rank3.previous_sibling.previous_sibling # 해당 엘리먼트 기준으로 이전 이전
#print(rank2.a.get_text())
#print(rank3.a.get_text())

#print(rank1.parent) # rank1 기준으로 부모로 이동

#rank2 = rank1.find_next_sibling("li")   # 태그 사이에 개행 정보등이 있어서 몇 번 next_sibling을 해야할지 모를 경우나 next_sibling을 여러번 사용하는것을 원치 않는 경우 사용
#print(rank2.a.get_text())

#print(rank1.find_next_siblings("li"))

#ranks = rank1.find_next_siblings("li")
#
#print(rank1.a.get_text())
#for rank in ranks:
#    print(rank.a.get_text())

webtoon = soup.find("a", text="독립일기-37화 게스트하우스")
print(webtoon.get_text())
