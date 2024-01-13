a,b,c = map(int,input('nhap a, b và c vao phuong trinh co dang ax^2+bx+c=0: ').split())
denta = (b**2)-(4*a*c)
x1 = None
x2 = None
if denta > 0:
    x1 = ( -b + denta**0.5) / 2*a
    x2 = ( -b - denta**0.5) / 2*a
elif denta == 0:
    x1 = -b / 2*a
    x2 = - b / 2*a
else:
    x = ' phương trình vô nghiệm'
if denta < 0:
    print(x)
else:
    print("nghiệm của phương trình là: ",x1,x2)
