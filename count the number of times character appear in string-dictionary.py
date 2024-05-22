#to count the number of times a character appears in given string using dictionary

str=input("enter the string:")
d={}
for i in str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print("number of times a character appears in given string:",d)
