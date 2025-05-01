import datetime as dt
from datetime import datetime
import pytz





Berlin_time = datetime(1992,10,5,17,30,30)
berlin_tz = pytz.timezone('Europe/Berlin')
auckland_tz = pytz.timezone('Pacific/Auckland')
localized_berlin_time = berlin_tz.localize(Berlin_time)


auckland_time = localized_berlin_time.astimezone(auckland_tz)

print("Berlin time:", localized_berlin_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Auckland time:", auckland_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))


# Task 2 convert date to each zone 
Moscow_time = datetime(2021,8,1,13,35,00) # اینجا تاریخ که میخواهیم تبدیل کنیم را وارد میکنمی 
moscow_tz = pytz.timezone('Europe/Moscow') # اینجا هم کد زون که تایم مربوط او میشه را وارد میکنیم
Moscow_newtime = moscow_tz.localize(Moscow_time) # اینجا بعدا تاریخ دستی را تبدیل به یک تاریخ رسمی میکنیم باید حتما این کار بشه 
berlin_tz = pytz.timezone('Europe/Berlin') # اینجا هم کد کشور که قصد داریم تبیدل بشه ه او وارد میکنیم
south_africa_tz = pytz.timezone('Africa/Johannesburg')
irish_tz = pytz.timezone('Europe/Dublin')
usa_tz = pytz.timezone('America/Los_Angeles')

curenttime_berlin = Moscow_newtime.astimezone(berlin_tz) # این کد هم تایل که رسمی شد و سیستم شنات را به تایم برلین تبدیل میکنه
Africa_time = Moscow_newtime.astimezone(south_africa_tz)
irish_time= Moscow_newtime.astimezone(irish_tz)
Usa_time = Moscow_newtime.astimezone(usa_tz)
print("Moscow time:", Moscow_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("German participants will meet at:", curenttime_berlin.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("South African participants will meet at::", Africa_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Irish participants will meet:", irish_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("American participants will meet at:", Usa_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

#.....................................................

# Task3 

timestamp = 1626430738

read_date = dt.datetime.fromtimestamp(timestamp)

Final_date = read_date.strftime('%Y-%m-%d %H:%M:%S')

print("Readable date:", Final_date)



