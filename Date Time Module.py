#Datetime
import datetime
x=datetime.datetime(2020,11,4)
#The day of datetime
print(x.strftime("%A"))
#The (lowcase ver.) day of datetime
print(x.strftime("%a"))
#The number order to the date of datetime
print(x.strftime("%w"))
#The week of datetime
print(x.strftime("%W"))
#The year of datetime
print(x.strftime("%y"))
#The (lowcase ver.) year of datetime
print(x.strftime("%Y"))
#The Current date of datetime
print(x.strftime("%x"))
#The Current time of datetime
print(x.strftime("%X"))
#The Current date and time of datetime
print(x.strftime("%c"))


#Return all properties and methods of datetime, without the values
print(dir(datetime)) 

#print current date and time
from datetime import date
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

#print inserted time (hour, minute, second, milisecond)
from datetime import time
a=time()
print(a)
b=time(2,44,56)
print(b)
c=time(1,34,55,5847)
print(c)
print(c.hour)
print(c.minute)
print(c.second)
print(c.microsecond)

#date as string 
from datetime import datetime
dateAsString='5 July, 2020'
date=datetime.strptime(dateAsString, "%d %B, %Y")
print(date)