day =int(input('nhập số nguyên bất kì trong khoảng 1...7: '))
if day == 1:
    weeks = 'Sunday'
elif day == 2:
    weeks = 'Monday'
elif day == 3:
    weeks = 'Tuesday'
elif day == 4:
    weeks = 'Wednesday'
elif day == 5:
    weeks = 'Thursday'
elif day == 6:
    weeks = 'Friday'
else:
    weeks = 'Saturday'
print(weeks)