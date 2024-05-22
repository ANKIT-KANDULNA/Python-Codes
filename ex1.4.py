#Python Program to Check if a Number is a Palindrome
s= input("Please enter the string/number: ")
reverse=s[::-1]
if reverse==s[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

#output
#Please enter the string/number: 121
#This is a palindrome
    
