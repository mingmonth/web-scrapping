import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

first_cartoon = soup.find("td", attrs={"class":"title"})
cartoons = soup.find_all("td", attrs={"class":"title"})
#print(cartoons[0].a.get_text())
#print("https://comic.naver.com" + cartoons[0].a["href"])

#cartoon_info = cartoons[0].parent#

#print(cartoon_info)
#print(cartoon_info.find("td", attrs={"class":"title"}))
#print(cartoon_info.find("div", attrs={"class":"rating_type"}).strong.get_text())
#print(rating.next_siblings("td"))

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    rating = cartoon.parent.find("div", attrs={"class":"rating_type"}).strong.get_text()
    print(title, link, rating)  
 
   

