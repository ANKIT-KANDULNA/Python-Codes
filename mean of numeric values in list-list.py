#mean of numeric values in a list

L1=[]
x=int(input("enter the number of elements:"))

for i in range(x):
    n=int(input("enter the element:"))
    L1.append(n)            

print(L1)
print(sum(L1))
print("mean of list is:",sum(L1)/n)
            
