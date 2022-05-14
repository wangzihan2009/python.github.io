q=float(input("请输入温度单位（摄氏度:1/华氏度:2/开尔文:3)"))
w=float(input("请输入转换后的温度单位(摄氏度:1/华氏度:2/开尔文:3)"))
if q==1:
    C = float(input("摄氏度"))
    F = 1.8*C+32
    K = C+273.15
    if w==2:
        print("华氏度:",F)
    elif w==1:
        pass
    else:
        print("开尔文:",K)
if q==2:
    f=float(input("华氏度"))
    c=(f-32)/1.8
    k=(f-32)/1.8+273.15
    if w==1:
        print("摄氏度:",c)
    elif w==2:
        pass
    else:
        print("开尔文:",k)
if q==3:
    a=float(input("开尔文"))
    b=a-273.15
    d=1.8*b+32
    if w==2:
        print("华氏度:",d)
    elif w==3:
        pass
    else:
        print("摄氏度:",b)
print("按d退出")
import msvcrt
print("Press 'D' to exit...")
while True:
    if ord(msvcrt.getch()) in [68, 100]:
        break