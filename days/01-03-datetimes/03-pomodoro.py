#!python3

from datetime import datetime
# from datetime import date
from datetime import timedelta

pomodoros = 0
pom_delta = timedelta(minutes=25)
break_delta = timedelta(minutes=3)
bigbreak_delta = timedelta(minutes=30)
task = ""

alarm = datetime.today() + pom_delta

while 1:
    if datetime.today() > alarm:
        print("Times up! Have a 3 minute break.")
        pomodoros += 1
        alarm = datetime.today() + break_delta
    else:
        print("Good work have a 30 minute break!")
        pomodoros = 0
        alarm = datetime.today() + bigbreak_delta








# 1. What is the task to be done?
# 2. Set the pomodoro timer to 25 minutes
# 3. Works on the task
# 4. End the work when the timer rings and tally 1
# 5. If the timer rings and there are < 4 tallys then have a 3 minute break
# 6. Else if the tally is more than 3 then have a 30 minute break
# 7. when the 30 min break is up go to step 1
