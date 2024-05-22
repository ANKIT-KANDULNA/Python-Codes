sub1=int(input("Enter marks of the first subject:"))
sub2=int(input("Enter marks of the second subject:"))
sub3=int(input("Enter marks of the third subject:"))
sub4=int(input("Enter marks of the fourth subject:"))
sub5=int(input("Enter marks of the fifth subject:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("Average Percentage",avg)
if(avg>=80):
    print("Grade:A")
elif(avg>=65):
    print("Grade:B")
elif(avg>=50):
    print("Grade:C")
elif(avg>=35):
    print("Grade:D")
else:
    print("Grade:F")
