with open("test.txt","r") as f:
    l=f.readlines()
    print(l)
    n=f.tell()
    print('n:',n)
print(f.closed)
