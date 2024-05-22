import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='ankit',database='restaurant')
cursor=con.cursor()
query="update dishes set half=30 where name='pav bhaji' "
cursor.execute(query)
con.commit()
print("data updated sucesssfully")
