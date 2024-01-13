N = str(input('nhập số nguyên dương N: '))
tong = 0
for i in range(len(N)):
    tong = (int(N[i])) + tong
print("tổng của các phần tử trong số nguyên dương N là: ", tong)
