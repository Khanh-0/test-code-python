temp = int(input("vui lòng nhập nhiệt độ: "))
if temp < 0:
    t = 'then Freezing weather'
elif temp < 10:
    t = 'then Very Cold weather'
elif temp < 20:
    t = 'then Cold weather'
elif temp < 30:
    t = 'then Normal in Temp'
elif temp < 40:
    t = 'then Its Hot'
else:
    t = 'then Its Very Hot'
print("Temp",temp,t)