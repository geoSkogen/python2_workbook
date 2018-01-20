import time
import calendar

localtime = time.localtime(time.time())

print(localtime)

format_time = time.asctime(time.localtime(time.time()))

print(format_time)

cal =  calendar.month(2016, 11)

print(cal)
