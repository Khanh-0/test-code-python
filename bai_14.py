ngay=int(input('vui long nhap ngay: '))
nam = None
tuan = None
nam = ngay // 365
tuan = (ngay - (nam * 365)) // 7
ngay = ngay - nam * 365 - tuan * 7
print("Years: ", nam,"\n""Weeks: ",tuan,"\n""Days: ",ngay)