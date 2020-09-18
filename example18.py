import datetime as dt
today = dt.datetime.today()
for i in range(1, 6):
    nextday = today + dt.timedelta(days=i)
    print(nextday)