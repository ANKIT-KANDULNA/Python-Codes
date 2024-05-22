#Create a dictionary with the roll number, name and marks of n students in a
#class and display the names of students who have scored marks above 75.

d={}
x=int(input("enter number of students:"))

for i in range(x):
    print("enter details of student number",i+1)
    r=int(input("roll number:"))
    n=input("name:")
    m=int(input("marks:"))
    d[r]=[n,m]

print(d)

for j in d:
    if d[j][1]>75:
        print(d[j][0])
    
