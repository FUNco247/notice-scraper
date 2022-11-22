import requests
from bs4 import BeautifulSoup
from functions.save import saveToCsv

SMTECH_URL : str = "https://www.smtech.go.kr/front/ifg/no/notice02_list.do"

def getSMTECHPage(url : str):
    result  = []
    req = requests.get(url)
    text = req.text
    soup = BeautifulSoup(text,"html.parser")
    table = soup.find("tbody", {})
    rows = table.find_all("tr")
    for row in rows:
        tds = row.find_all("td")
        #link = row.find("a").get("href")
        textArray=[]
        for td in tds:
            textArray.append(td.text.strip())
            #{"number" : textArray[0], "project": textArray[1], "subject": textArray[2], "duration" : textArray[3],"notice": textArray[4], "link": f"https://www.smtech.go.kr{link}" }
        result.append({"title": textArray[1], "date" : textArray[3]})
    return result

def get_SMTECH_csv():
    infos = getSMTECHPage(SMTECH_URL)
    saveToCsv("SMTECH", infos)