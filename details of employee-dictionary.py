#input details of n employees

emp={}
n=int(input("enter number of records:"))
i=1
while i<=n:
    name=input("enter the name:")
    basic=int(input("enter basic salary:"))
    hra=int(input("enter HRA"))
    emp[name]=[basic,hra]
    i+=1

print(emp)

k=emp.keys()
print('Name','\t\t','Total Salary')
for i in k:
    sal=0
    z=emp[i]
    for j in z:
        sal=sal+j
    print(i,'\t\t',sal)   
