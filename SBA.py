import requests
from bs4 import BeautifulSoup

SBA_URL : str = "https://www.sba.seoul.kr/Pages/ContentsMenu/Company_Support.aspx?C=6FA70790-6677-EC11-80E8-9418827691E2"

def getSBAPage(url : str):
    req = requests.get(url)
    text = req.text
    soup = BeautifulSoup(text,"html.parser")
    table = soup.find("div",{"id":"container"}).find("div",{"class":"content"}).find("div",{"id":"card_list"}).findChildren()
    print(table)

getSBAPage(SBA_URL)