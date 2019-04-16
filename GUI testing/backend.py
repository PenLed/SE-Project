# cnx = mysql.connector.connect(user='root', password='Catharsys@1993',
#                               host ='localhost', database='students')

import mysql.connector

mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "Carlyssa4me",
			database="lms"
	)

mycursor = mydb.cursor()
mycursor.execute("SELECT student_username FROM student_login")
usernames = mycursor.fetchall() 
usernames =[i[0] for i in usernames]

mycursor.execute("SELECT student_password FROM student_login")
passwords = mycursor.fetchall() 
passwords =[i[0] for i in passwords]

# variable = 'mendeza37'
# mycursor.execute("SELECT first_name FROM student_information WHERE student_username = %s",(variable,))
# # cursor1.execute("SELECT * FROM People WHERE Name=%s", (myName,))
# database = mycursor.fetchall()
# print (database)



# for row in usernames:
# 	print(row)