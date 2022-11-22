import csv
from functions.getDate import getCurrenDate


def saveToCsv(name, infos):
    date = getCurrenDate()
    file = open(f"csv/{name}/{date}.csv", mode="w",encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["title","date"])
    for info in infos:
        writer.writerow([info["title"], info["date"]])
    return
