#frequency of a number in a list

list1=eval(input("enter the list:"))
length=len(list1)

ele=int(input("enter the no. to be counted:"))
count=0

for i in range(0,length):
    if ele==list1[i]:
        count+=1

if count==0:
    print(ele,"is counted 0 times")
else:
    print(ele,"is counted",count,"times")
    

