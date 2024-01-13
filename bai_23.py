year=int(input('vui lòng nhập số năm cần tính toán: '))
if year % 4 == 0 and year % 100 != 0:
    s = ' is a leap year'
else:
    s = ' is not a leap year'
print(str(year)+s)