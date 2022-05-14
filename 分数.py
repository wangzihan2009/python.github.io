import msvcrt
print("-1不计入")
A=float(input("语文成绩:"))
B=float(input("数学成绩:"))
C=float(input("英语成绩:"))
D=float(input("科学成绩:"))
E=float(input("历社成绩:"))
if A==-1 or B==-1 or C==-1 or D==-1 or E==-1:
    f=A*0
    g=B*0
    h=C*0
    i=D*0
    j=E*0
    if A==-1:
        H=(f+B+C+D+E)//1
        print("总分为:",H)
    elif B==-1:
        H=(A+g+C+D+E)//1
        print("总分为:",H)
    elif C==-1:
        H=(A+B+h+D+E)//1
        print("总分为:",H)
    elif D==-1:
        H=(A+B+C+i+E)//1
        print("总分为:",H)
    elif E==-1:
        H=(A+B+C+D+j)//1
        print("总分为:",H)
    elif A==-1 and B==-1:
        H=(f+g+C+D+E)//1
        print("总分为:",H)
    elif B==-1 and C==-1:
        H=(A+g+h+D+E)//1
        print("总分为:",H)
    elif C==-1 and D==-1:
        H=(A+B+h+i+E)//1
        print("总分为:",H)
    elif D==-1 and E==-1:
        H=(A+B+C+i+j)//1
        print("总分为:",H)
    elif A==-1 and C==-1:
        H=(f+B+h+D+E)//1
        print("总分为:",H)
    elif A==-1 and D==-1:
        H=(f+B+C+i+E)//1
        print("总分为:",H)
    elif A==-1 and E==-1:
        H=(f+B+C+D+j)//1
        print("总分为:",H)
    elif B==-1 and D==-1:
        H=(A+g+C+i+E)//1
        print("总分为:",H)
    elif B==-1 and E==-1:
        H=(A+g+C+D+j)//1
        print("总分为:",H)
    elif C==-1 and E==-1:
        H=(A+B+h+D+j)//1
        print("总分为:",H)
    elif A==-1 and B==-1 and C==-1:
        H=(f+g+h+D+E)//1
        print("总分为:",H)
    elif A==-1 and B==-1 and D==-1:
        H=(f+g+C+i+E)//1
        print("总分为:",H)
    elif A==-1 and B==-1 and E==-1:
        H=(f+g+C+D+j)//1
        print("总分为:",H)
    elif A==-1 and C==-1 and D==-1:
        H=(f+B+h+i+E)//1
        print("总分为:",H)
    elif A==-1 and C==-1 and E==-1:
        H=(f+B+h+D+j)//1
        print("总分为:",H)
    elif A==-1 and D==-1 and E==-1:
        H=(f+B+C+i+j)//1
        print("总分为:",H)
    elif B==-1 and C==-1 and D==-1:
        H=(A+g+h+i+E)//1
        print("总分为:",H)
    elif B==-1 and C==-1 and E==-1:
        H=(A+g+h+D+j)//1
        print("总分为:",H)
    elif C==-1 and D==-1 and E==-1:
        H=(A+B+h+i+j)//1
        print("总分为:",H)
    elif A==-1 and B==-1 and C==-1 and D==-1:
        H=(f+g+h+i+E)//1
        print("总分为:",H)
    elif E==-1 and B==-1 and C==-1 and D==-1:
        H=(A+g+h+i+j)//1
        print("总分为:",H)
    elif A==-1 and B==-1 and C==-1 and D==-1 and E==-1:
        print("按d退出")
        while True:
            if ord(msvcrt.getch()) in [68, 100]:
                break 
else:
    F=(A+B+C+D+E)//1
    print("总分为:",F)
a=(A/150)*100//1
b=(B/150)*100//1
c=(C/110)*100//1
d=(D/170)*100//1
e=(E/80)*100//1
print("正确率：")
if B==-1:
    pass
else:
    print("数学：","%.0f%%" % b)
if A==-1:
    pass
else:
    print("语文：","%.0f%%" % a)
if C==-1:
    pass
else:
    print("英语：","%.0f%%" % c)
if D==-1:
    pass
else:
    print("科学：","%.0f%%" % d)
if E==-1:
    pass
else:
    print("历社：","%.0f%%" % e)
print("按d退出")
while True:
    if ord(msvcrt.getch()) in [68, 100]:
        break