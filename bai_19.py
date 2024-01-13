number =float(input('nhập số cần tính: '))
if number == 0:
    t="number is zero"
elif number < 0:
    t="number is negative"
else:
    t="number is positive"
print(t)