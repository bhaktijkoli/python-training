import datetime as dt
today = dt.datetime.today()
yesterday = today - dt.timedelta(days=1)
tomorrow = today + dt.timedelta(days=1)

print("Yesterday", yesterday)
print("Today", today)
print("Tomorrow", tomorrow)