import datetime
import pytz

today = datetime.date.today()
print(today)

birthday =datetime.date(2000, 9 ,16 )
print(birthday)

days_since_birth =( today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)

print(today +tdelta)
print(today.month)
print(today.day)
print(today.weekday())

print(datetime.time())
#.date ymd  .time  h m s ms  .datetime  ymd h m s ms
#add 10 hrs to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific =datetime_today.astimezone(pytz.timezone("US/Pacific"))
print(datetime_pacific)
'''
for tz in pytz.all_timezones:
    print(tz)
'''
#string formatting with dates 
# 2020-03-09 -> march 9 ,2020

print(datetime_pacific.strftime("%B %d,%Y"))

datetime_thing = (datetime.datetime.strptime("August 21 , 2020" ,"%B %d , %Y"))
print(datetime_thing)

#also rrefer to maya which is better can be done for space projects
#pip install pytz for time zone
print("done")
