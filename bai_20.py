a,b,c=map(float,input('nhập 3 số cần so sánh: ').split())
if a > b and a > c:
    t = a
elif b > c:
    t = b
else:
    t = c
print("số lớn nhất là: ",t)