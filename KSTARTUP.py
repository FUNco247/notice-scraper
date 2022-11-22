from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

KSTARTUP_URL : str = "https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do"
driver = webdriver.Chrome(ChromeDriverManager().install())

def getKSTARTUPPage(url : str):
    result  = []
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    lists = soup.find("div",{"class":"board_list-wrap"}).find_all("li",{"class":"notice"})
    for li in lists:
        content = li.find("div",{"class":"right"})
        title = content.find("p",{"class":"tit"}).text
        date = content.find("div",{"class":"bottom"}).find_all("span")
        dateStart = date[2].text.split()[1]
        dateEnd = date[3].text.split()[1]
        duration = f"{dateStart}~{dateEnd}"
        info = {"title":title, "date":duration}
        result.append(info)
    print(result)

getKSTARTUPPage(KSTARTUP_URL)