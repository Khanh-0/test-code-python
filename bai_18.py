int_number = int(input('nhập số nguyên: '))
if int_number % 2 == 0 and int_number !=0:
    t="number is even"
elif int_number % 2 != 0 and int_number!=0:
    t ="number is odd"
else:
    t="number is neither even nor odd"
print(t)