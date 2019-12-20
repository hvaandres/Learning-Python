import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019, 3))

print(calendar.calendar(2019))

day_of_the_week = calendar.weekday(2019, 3, 14)
print(day_of_the_week)

is_leap =calendar.isleap(2019)
print(is_leap)

how_many_leap_days = calendar.leapdays(2018,2019)
print(how_many_leap_days)