from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from functions.save import saveToCsv

SBA_URL : str = "https://www.sba.seoul.kr/Pages/ContentsMenu/Company_Support.aspx?C=6FA70790-6677-EC11-80E8-9418827691E2"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

def getSBAPage(url : str):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("div",{"id":"card_list"})
    cards = table.find_all("div",{"class":"card_box"})
    result = []
    for card in cards:
        title = card.find("a").text
        date = card.find("dd",{"class":"date"}).text
        info = {"title" : title, "date":date}
        result.append(info)
    return result

def get_SBA_csv():
    infos = getSBAPage(SBA_URL)
    saveToCsv("SBA", infos)