import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")  # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=blackpink")
time.sleep(5)  # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, "html.parser")

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    img = thumbnail["src"]
    dload.save(img, f"img/{i}.jpg")
    i += 1

driver.quit()  # 끝나면 닫아주기
