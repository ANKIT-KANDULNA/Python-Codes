#smallest element from a tuple without using built-in function.

L1=[]
n=int(input("enter the number of elements:"))

for i in range(n):
    m=int(input("enter the elements:"))
    L1.append(m)
    
T1=tuple(L1)
print(T1)
sorted(T1)
T=sorted(T1)
print("smallest element is:",T[0])


    



   



