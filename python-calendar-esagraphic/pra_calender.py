# Write a program that takes a date as input and checks if that date falls on a weekend (Saturday or Sunday).
import calendar
from datetime import datetime
# entered_date = input('Please enter your date ')

# date_convert= datetime.strptime(entered_date,'%Y-%m-%d')
# if date_convert.weekday() >= 5:
#     print(f"{entered_date} is a weekend.")
# else:
#     print(f"{entered_date} is not a weekend.")



# Task 2 

year = 2024
month = 7
# year_convert= datetime.strptime(year,'%Y')


first_day = datetime(year,month,1)
last_day_num = calendar.monthrange(year, month)
last_day = datetime(year, month, last_day_num)

print("First day of the month:", first_day.strftime('%Y-%m-%d'))
print("Last day of the month:", last_day.strftime('%Y-%m-%d'))