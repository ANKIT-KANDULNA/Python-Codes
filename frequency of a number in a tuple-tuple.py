#count the frequency of an element in Tuple.

L1=[]
n=int(input("enter the number of elements:"))

for i in range(n):
    m=int(input("enter the element:"))
    L1.append(m)
    
T1=tuple(L1)
print(T1)
c=int(input("which element you want to count:"))
print("frequency of element is:",T1.count(c))

