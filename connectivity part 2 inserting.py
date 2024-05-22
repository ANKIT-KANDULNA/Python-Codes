import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='ankit',database='restaurant')
cur=con.cursor()
n=int(input("enter number of record you want to insert"))
for i in range(n):
    name=input("enter name of your dish")
    half=int(input("enter the price"))
    full=int(input("enter the price"))
    query="insert into dishes(name,half,full)values('{}',{},{})".format(name,half,full)
    cur.execute(query)
    con.commit()
    print("data inserted sucessfully..........")
