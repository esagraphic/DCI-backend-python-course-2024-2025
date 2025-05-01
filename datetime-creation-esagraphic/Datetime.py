import datetime as dt 
# Task 1 Print The Curent Year 

curent_datetime = dt.datetime.now()
print(curent_datetime.year)

#....................................................
# Task 2 Using the variable called some_date, print out the current week day

some_date = dt.datetime(2021, 7, 14)
print(some_date.weekday())

#Task 3 Write a Python program to determine whether the year 2021 is a leap year.


def is_leap_year(year):
    try:
        dt.datetime(year, 2, 29)
        return True
    except ValueError:
        return False

year = 2021
is_leap = is_leap_year(year)
print(f"{year} is a leap year? {'Yes' if is_leap else 'No'}")


# next Method 
import calendar

year = 2022
is_leap_year = calendar.isleap(year)
print(f"Is {year} a leap year? {is_leap_year}")


# Task 4 Your task is to convert a user provided string into a datetime object.

date_as_string = "Feb 14 2021 8:30AM"

Converted_date = dt.datetime.strptime(date_as_string,'%b %d %Y %I:%M%p')
print(Converted_date)
