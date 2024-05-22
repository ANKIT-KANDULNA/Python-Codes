#Python Program to Take in the Marks of 5 Subjects and Display the Grade 
m1=int(input("enter the marks in sub1:"))
m2=int(input("enter the marks in sub2:"))
m3=int(input("enter the marks in sub3:"))
m4=int(input("enter the marks in sub4:"))
m5=int(input("enter the marks in sub5:"))
avg=(m1+m2+m3+m4+m5)/5
print(avg)
if (avg>=80):
    print("A grade")
elif (avg>=65 & avg<80):
    print("B grade")
elif (avg>=51 & avg<65):
    print("C grade")
elif (avg>=36 & avg<50):
    print("D grade")
else:
    print("E grade")

#output
#enter the marks in sub1:75
#enter the marks in sub2:82
#enter the marks in sub3:89
#enter the marks in sub4:72
#enter the marks in sub5:88
#81.2
#A grade
