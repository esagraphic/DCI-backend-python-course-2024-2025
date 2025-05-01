#List of months: January, February, March, April, May, June, July, August, September, October, November, December


Month_Name = input('Input The name of Month: ').capitalize()

if Month_Name in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
    print('Number of Days: 31 days')
elif Month_Name in ['April', 'June', 'September', 'November']:
    print('Number of Days: 30 days')
elif Month_Name == 'February':
    print('Number of Days: 28 or 29 days')
else:
    print(f"'{Month_Name}' is not a valid month name.")




