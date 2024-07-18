#Date and Time in Python
import datetime as dt


curent_date=dt.date.today()

print("Today Date: ",curent_date)

new =dt.date(2023,11,12)

print("Date: ",new)
print("Year: ",new.year)
print("Month: ",new.month)
print("Day: ",new.day)
print("<------------------------------------------>")

a=dt.datetime.now()

print("Current Date & Time: ",a)