from datetime import datetime

def isweekend(date):
    day_of_week = date.strftime('%A')
    # print(day_of_week)
    return True if day_of_week == 'Saturday' or day_of_week == 'Sunday' else False

date = datetime(2021, 8, 7)

print(isweekend(date))