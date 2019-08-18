import datetime


current = datetime.datetime.now()
for i in range(20):
    print((current + datetime.timedelta(days=7*i)).strftime("%Y-%m-%d"))
