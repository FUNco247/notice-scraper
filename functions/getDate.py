import datetime

def getCurrenDate():
    date = datetime.datetime.now()
    return str(date)[:10]