import requests
import re
from bs4 import BeautifulSoup

for i in range(1, 6):
    print("페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Referer":"https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            #print(" <광고 상품 제외합니다>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # 애플 제품 제외
        if "Apple" in name or "apple" in name:
            #print(" <Apple 상품 제외 합니다>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()

        # 리뷰 50 개 이상, 평점 4.5 이상 되는 것만 조회

        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = ""
            #print(" <평점 없는 상품 제외합니다>")
            continue
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            rate_cnt = ""
            #print(" <리뷰 없는 상품 제외합니다>")
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 50:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄긋기
        # else:
        #     print(" <평점이나 리뷰수가 만족되지 않는 상품입니다>")
