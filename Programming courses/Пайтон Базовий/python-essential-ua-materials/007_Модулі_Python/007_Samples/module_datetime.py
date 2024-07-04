from datetime import datetime

now = datetime.now()
print(now)
print(datetime.time(now))
print(now.year, now.month, now.day)

date_string = "21 June, 2018"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
