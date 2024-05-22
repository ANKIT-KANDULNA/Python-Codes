# largest number in a list

L1=[]
n=int(input("enter the number of elements in the list:"))

for i in range(n):
   m=int(input("enter the element:"))
   L1.append(m)

L1.sort()
print(L1)
print("largest element is:",L1[-1])


   



