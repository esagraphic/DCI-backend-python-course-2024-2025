from datetime import datetime

def isweekend(date):
    day_of_week = date.strftime('%A')
    # print(day_of_week)
    return True if day_of_week == 'Saturday' or day_of_week == 'Sunday' else False

date = datetime(2021, 8, 7)



username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
# Your code here

if isweekend(date) or username == valid.get('username') and password == valid.get('username'):
    print(f'Welcome ,{username}')
else:
    print('Credentials are invalid')


# note This code uses logical operators (or and and), which follow short-circuit evaluation. This means that once the outcome of a condition is determined, the remaining conditions might not be evaluated.
