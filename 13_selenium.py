import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
# browser.find_element_by_id("id").send_keys("ys9922")
# time.sleep(1)
# browser.find_element_by_id("pw").send_keys("hero801107")

# 3. 우회 방법
tag_id = browser.find_element_by_name("id")
tag_pw = browser.find_element_by_name("pw")
tag_id.clear()

time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy("naver_id")
tag_id.send_keys(Keys.CONTROL, "v")
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy("naver_pw")
tag_pw.send_keys(Keys.CONTROL, "v")
time.sleep(1)

# 4. 로그인 버튼 클릭
elem = browser.find_element_by_id("log.login").click()

#time.sleep(3)

# 5. id 를 새로 입력
#browser.find_element_by_id("id").clear()
#browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
#print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
#browser.quit() # 브라우저 종료



