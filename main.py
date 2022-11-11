import requests
import urllib
from bs4 import BeautifulSoup

SMTECH_URL = "https://www.smtech.go.kr/front/ifg/no/notice02_list.do"

def getPage(url):
    result = []
    req = requests.get(url)
    text = req.text
    soup = BeautifulSoup(text,"html.parser")
    table = soup.find("tbody", {})
    rows = table.find_all("tr")
    for row in rows:
        tds = row.find_all("td")
        link = row.find("a").get("href")
        textArray=[]
        for td in tds:
            textArray.append(td.text.strip())
        result.append({"number" : textArray[0], "project": textArray[1], "subject": textArray[2], "duration" : textArray[3],"notice": textArray[4], "link": link })
    return print(result)

getPage(SMTECH_URL)