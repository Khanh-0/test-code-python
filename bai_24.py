a,b = map(int,input('nhap a va b vao phuong trinh co dang ax+b=0: ').split())
if a == 0:
    print("phương trình vô nghiệm")
elif b>0:
    B= str('+')
    print("ket qua cua phuong trinh", str(a) + "x", B, b, "= 0 la x =", (-b / a))
else:
    B = str('-')
    b=b * -1
    print("ket qua cua phuong trinh",str(a)+"x",B,b,"= 0 la x =",(-b/a))