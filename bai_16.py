h,canh_day,canh_b,canh_c= map(int,input('nhập chiều cao H cạnh đáy và hai cạnh còn lại của hình tam giác: ').split())
canh_hinh_vuong =int(input('vui lòng nhập độ dài cạnh hình vuông: '))
dai_chu_nhat,rong_chu_nha = map(int,input('nhập chiều dài và rộng của chình chữ nhật: ').split())
S_tam_giac = (1/2)*h*canh_day
P_tam_giac = canh_b+canh_c+canh_day
S_hinh_vuong = canh_hinh_vuong**2
P_hinh_vuong = 4*canh_hinh_vuong
S_chu_nhat = dai_chu_nhat*rong_chu_nha
P_chu_nhat = 2*(dai_chu_nhat*rong_chu_nha)
print("diện tích và chu vi lần lược của các hình:\n"
      "Tam giác:",S_tam_giac,"và",P_tam_giac,"\n"
      "Hình vuông:",S_hinh_vuong,"và",P_hinh_vuong,"\n"
      "Hình chữ nhật:",S_chu_nhat,"và",P_chu_nhat)