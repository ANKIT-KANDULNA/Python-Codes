#to input names of countries and their capital and currency. Search for a particular country

d={}
x=int(input("enter number of countries:"))

for i in range(x):
    print("enter country name:",i+1)
    o=input("country:")
    a=input("capital:")
    u=input("currency:")
    d[o]=[a,u]

print(d)
n=input("which country you want to search:")
print(d.get(n))

    
