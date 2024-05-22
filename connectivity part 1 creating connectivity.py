import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='ankit',database='restaurant')
if  con.is_connected():
    print("Sucessfully connected...........")
