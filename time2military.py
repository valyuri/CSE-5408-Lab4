# Lab 4 Part C Current time in military time
# Uriel Gonzalez
from datetime import datetime

#gets the current time and displays the 12 hour and military time format
def militaryTime():
    currentTime = datetime.now()

    twelvehour = currentTime.strftime('%I:%M %p')
    print('Current 12h Time: ', twelvehour)

    militaryTime = currentTime.strftime('%H:%M')
    print('Current Military Time: ', militaryTime)

militaryTime()