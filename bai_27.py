n= int(input('vui lòng nhập số cần tính: '))
s1 = int(n%10)
s2 = int(((n - s1)/10)%10)
s3 = int(n//100)
if s1 > s2 and s1 > s3:
    max = s1
elif s2 > s3:
    max = s2
else:
    max = s3

if s1 < s2 and s1 < s3:
    min = s1
elif s2 < s3:
    min = s2
else:
    min = s3
giua = int((s1+s2+s3)-min-max)
print(str(min)+str(giua)+str(max))