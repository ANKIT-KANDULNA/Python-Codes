# Program to make a Calculator.

import math
import statistics

print("* * * C A L C U L A T O R * * *")
print("Assigning different values to different functions:")
print("1=Math",'\t',"2=Trigonometry",'\t',"3=Statistics",'\t',"4=Simple Calculation")
print("11=pi",'\t',"21=sin()",'\t','\t',"31=mean()",'\t',"41=addition")
print("12=e",'\t',"22=cos()",'\t','\t',"32=median()",'\t',"42=substraction")
print("13=ceil",'\t',"23=tan()",'\t','\t',"33=mode()",'\t',"43=multiplication")
print("14=floor",'\t','\t','\t','\t','\t',"44=division")
print("15=pow(x,y)")
print("16=sqrt()")
print("17=fabs()")
print("18=log10()")

#'t' is for tab space.

while True:
    choice=int(input("enter your choice(1/2/3/4):")) 
    if choice in (1,2,3,4):
        if choice==1:
            print("which math function you want to use:")
            while True:
                chose=int(input("enter your choice(11,12,13,14,15,16,17,18):"))
                if chose in (11,12,13,14,15,16,17,18):
                    if chose==11:
                        print("value of pi is:",math.pi) 
                    elif chose==12:
                        print("value of euler's number is:",math.e) 
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
                        print("fabs function:",math.fabs(p)) 
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
        elif choice==4:
            print("which simple calculation function you want to use:")
            while True:
                coose=int(input("enter your choice(41,42,43,44):"))
                if coose in (41,42,43,44):
                    if coose==41:
                        a=int(input("enter the number1:"))
                        b=int(input("enter the number2:"))
                        print("addition of the numbers is:",a+b) 
                    elif coose==42:
                        c=int(input("enter the number1:"))
                        d=int(input("enter the number2:"))
                        print("subtraction of the numbers is:",c-d) 
                    elif coose==43:
                        e=int(input("enter the number1:"))
                        f=int(input("enter the number2:"))
                        print("multiplication of the number is:",e*f) 
                    elif coose==44:
                        i=int(input("enter the number1:"))
                        j=int(input("enter the number2:"))
                        print("division of the number is:",i/j) 
                    else:
                        print("function not found")
                    break
    else:
        print("function not found")
    break


