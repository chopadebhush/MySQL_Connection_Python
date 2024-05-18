import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
con = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
cursor =con.cursor()
cursor.execute(")
for i in cursor.fetchall():
  print(i)

