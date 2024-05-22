#swap elements at the even location with the elements at the odd location

lst1=[]

m=int(input("enter number of element:"))
for i in range(m):
    num=int(input("enter number"))
    lst1.append(num)

print("before swapping:",lst1)

for n in range(0,m,2):
    tmp1=lst1[n]
    tmp2=lst1[n+1]
    lst1[n]=tmp2
    lst1[n+1]=tmp1
    
print("after swapping:",lst1)                  
