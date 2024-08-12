import calendar
weekday = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
m,d,y = map(int,input().split())
a=calendar.weekday(y,m,d)
print(weekday[a])

# input-->  08 05 2015