n=int(input('nhập số lượng số cần so sánh: '))
# tạo mảng rỗng a
a = []
for i in range(n):
    a.append(float(input("nhập số thứ{} :".format(i+1))))
max = a[0]
for i in range(1, n):
         if a[i] > max:
            max = a[i]
print("vậy số lớn nhất trong dãy số là: ",max)