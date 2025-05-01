from datetime import datetime , timedelta
# Task 1 Using the variable called current_datetime, subtract 15 days from the current time.

current_datetime = datetime.now()
sub_date = timedelta(days=15)
new_date = current_datetime - sub_date
Final_date = new_date.strftime('%Y-%m-%d')
print(Final_date)
#-----------------------------------------------------------------------------

# Task 2 Using the variable called current_datetime, add 7 days to your current day.
add_date = timedelta(days=7)

add_new_date= current_datetime + add_date
Final_date_add = add_new_date.strftime('%Y-%m-%d')
print(Final_date_add)


#-----------------------------------------------------------------------------

# Task 3 Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.



from datetime import datetime, timedelta
import calendar

# Define the year and month
year = 2024
month = 7

# First day of the month
first_day = datetime(year, month, 1)

# Last day of the month
_, last_day_num = calendar.monthrange(year, month)
last_day = datetime(year, month, last_day_num)

print("First day of the month:", first_day.strftime('%Y-%m-%d'))
print("Last day of the month:", last_day.strftime('%Y-%m-%d'))

