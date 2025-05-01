
from datetime import datetime
def great ( name , date):
    noon = datetime.strptime('12:00', '%H:%M').time()
    time = date.time()
    if time < noon:
        return(f'Good Morning {name}')
    else:
        return(f'Good Afternoon: {name}')

date_insert = datetime(2021, 5, 7, 14, 59, 59)

print(great('Essa', date_insert))