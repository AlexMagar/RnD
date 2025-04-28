import calendar
import pandas

year = int(input('Enter Year: '))
month = int(input('Enter month: '))

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar(year))
rlt = calendar.calendar(year,2,1,6,4)
print(calendar.month(year,month))
print(rlt)

# calendar(theyear: int, w: int=..., l: int=..., c: int=..., m: int=...)
# theyear: int 
# w: int=..., width of the calendar columns
# l: int=..., line spacing 
# c: int=..., space between month
# m: int=..., How manu month to display in a row