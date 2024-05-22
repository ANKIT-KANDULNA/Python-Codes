n=int(input("Enter the number of term you want to print: "))
first=-1
second= 1
for i in range(n):
    third=first+second
    print(third,end=" ")
    first,second=second,third
