#!python3

from datetime import datetime
from datetime import date

today = datetime.today()

todaydate = date.today()

# printing today is the same as converting to string
print(today)
print(todaydate)

print(todaydate.day)
print(todaydate.month)
print(todaydate.year)
print()
print(today.day)
print(today.month)
print(today.year)
print(today.hour)
print(today.minute)
print(today.second)
