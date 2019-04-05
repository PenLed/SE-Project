# cnx = mysql.connector.connect(user='root', password='Catharsys@1993',
#                               host ='localhost', database='students')

import mysql.connector

mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "Catharsys@1993",
			database="students"
	)

mycursor = mydb.cursor()

mycursor.execute("SELECT username FROM student_log")

usernames = mycursor.fetchall() 
usernames =[i[0] for i in usernames]

mycursor.execute("SELECT password FROM student_log")

passwords = mycursor.fetchall() 
passwords =[i[0] for i in passwords]




# for row in usernames:
# 	print(row)