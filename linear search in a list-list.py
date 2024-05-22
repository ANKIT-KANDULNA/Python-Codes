#linear search on a list

list1=[]
n=int(input("enter the number of elements in the list:"))

for i in range(n):
   m=int(input("enter the element:"))
   list1.append(m)

print(list1)
n=int(input("enter the number to be found:"))

for i in range(len(list1)):
    if list1[i]==n:
        print("found at index",i)
        break

else:
    print("not found")
