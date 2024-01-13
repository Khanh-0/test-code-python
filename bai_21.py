a,b,c=map(float,input("nhập lần lượt 3 số cần so sánh: ").split())
Tmax= None
Tmin = None
if a > b and a > c:
    Tmax= a
elif b > c:
    Tmax = b
else:
    Tmax = c
if a < b and a < c:
    Tmin= a
elif b < c:
    Tmin = b
else:
    Tmin = c
T = (a+b+c)-Tmin-Tmax
print(Tmin,T,Tmax)