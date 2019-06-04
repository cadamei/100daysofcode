#!python3

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=25)

type(t)

# This will add the days and hours and print the number of days rounded down to the nearest day.
print(t.days)

# Since the seconds maxes out at 1 full day, printing 't.seconds' will print
# out the leftover hour(s) less than a full day
print(t.seconds)
print(t.seconds / 60 / 60)

# This does not work for ".hours" since seconds already exist. Maths above.
# Slightly confusing since it's not written "timedelta(days=4, seconds=3600)"
# Timedelta represents the time between two points

# The amount of time between two points
eta = timedelta(hours=8)

# The time when run
today = datetime.today()

print(today)
print(eta)

# To calculate the time plus eta at runtime simply add the two
print(today + eta)
