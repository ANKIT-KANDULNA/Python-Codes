n=int(input("Enter number of rows:"))
for i in range(n): #0,1,2,3
    for j in range(n-i):
        print(j+1,end=" ")
    print()
