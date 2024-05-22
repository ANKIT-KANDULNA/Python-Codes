#Python Program to Print all Numbers in a Range Divisible by a Given Number
l=int(input("enter the lower number:"))
u=int(input("enter the upper number:"))
n=int(input("enter the number you want to be divided by:"))
for i in range(l,u+1):
    if (i%n==0):
        print(i)
        
#output
#enter the lower number:1
#enter the upper number:50
#enter the number you want to be divided by:6
#6
#12
#18
#24
#30
#36
#42
#48        
