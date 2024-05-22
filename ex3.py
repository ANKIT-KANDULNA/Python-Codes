# program to calculate avg. marks of n students

list1 = []

print("how many students mark you want to enter:")

n=int (input())

for i in range (0,n) :
    print ("enter marks of students",(i+1),":")
    marks=int(input())
    list1.append(marks)
    print(list1)

for marks in list1:
    total=total+marks

avg=total/n
print("avg marks=", avg)
