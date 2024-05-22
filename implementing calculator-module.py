#to implement calculator functions using the concept of modules

import math
import statistics

print("*****CALCULATOR*****")
print("Assigning different values to different functions")
print("1=Math",'\t',"2=Trigonometry",'\t',"3=Statistics")
print("11=pi",'\t',"21=sin(x)",'\t',"31=mean()")
print("12=e",'\t',"22=cos(x)",'\t',"32=median()")
print("13=ceil()",'\t',"23=tan(x)",'\t',"33=mode()")
print("14=floor(x)")
print("15=pow(x,y)")
print("16=sqrt(x)")
print("17=fabs(x)")
print("18=log10(x)")

while True:
    choice=int(input("enter your choice(1/2/3):"))
    if choice in (1,2,3):
        if choice==1:
            print("which math function you want to use:")
            while True:
                chose=int(input("enter your choice(11,12,13,14,15,16,17,18):"))
                if chose in (11,12,13,14,15,16,17,18):
                    if chose==11:
                        print("value of pi is:",math.pi)
                    elif chose==12:
                        print("value of euler number is:",math.e)
                    elif chose==13:
                        x=float(input("enter the number:"))
                        print("ceil function:",math.ceil(x))
                    elif chose==14:
                        y=float(input("enter the number:"))
                        print("floor function:",math.floor(y))
                    elif chose==15:
                        m=int(input("enter the number:"))
                        n=int(input("enter the number:"))
                        print("power function:",math.pow(m,n))
                    elif chose==16:
                        z=int(input("enter the number:"))
                        print("square root:",math.sqrt(z))
                    elif chose==17:
                        p=int(input("enter the number:"))
                        print("fabs function:",math.fab(p))
                    elif chose==18:
                        q=int(input("enter the number:"))
                        print("logarithm function:",math.log10(q))
                    else:
                        print("function not found")
                    break
        elif choice==2:
             print("which trigonometric function you want to use:")
             while True:
                 choose=int(input("enter your choice(21,22,23):"))
                 if choose in (21,22,23):
                     if choose==21:
                         u=int(input("enter the number:"))
                         print("sine of the number is:",math.sin(u))
                     elif choose==22:
                        v=int(input("enter the  number:"))
                        print("cosine of the number is:",math.cos(v))
                     elif choose==23:
                        w=int(input("enter the number:"))
                        print("tangent of the number is:",math.tan(w))
                     else:
                        print("function not found:")
                     break
        elif choice==3:
            print("which statistics function you want to use:")
            while True:
                choos=int(input("enter your choice(31,32,33):"))
                if choos in (31,32,33):
                    if choos==31:
                        L1=[]
                        n=int(input("enter the number of elements in the list:"))
                        for i in range(n):
                            m=int(input("enter the element:"))
                            L1.append(m)
                        print("mean of list is:", statistics.mean(L1))
                    elif choos==32:
                        L1=[]
                        n=int(input("enter the number of elements in the list:"))
                        for i in range(n):
                            m=int(input("enter the element:"))
                            L1.append(m)
                        print("median of list is:", statistics.median(L1))
                    elif choos==33:
                        L1=[]
                        n=int(input("enter the number of elements in the list:"))
                        for i in range(n):
                            m=int(input("enter the element:"))
                            L1.append(m)
                        print("mode of list is:", statistics.mode(L1))
                    else:
                        print("function not found")
                    break
    else:
        print("function not found")
    break
