#wap to input n names and phone number to stor it in a dictionary.

phone={}
n=int(input("enter the number of records you want to store:"))
for i in range(n):
    a=input('enter name:')
    b=int(input("enter the number:"))
    phone[a]=b

print(phone)
