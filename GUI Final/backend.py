import mysql.connector
from mysql.connector import Error 
mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "Carlyssa4me",
			database="lms"
	)

sql_select_Query = "SELECT  * FROM class_grade WHERE student_id = '1' "
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
grades = cursor.fetchall()

sql_select_Query = "SELECT student_username FROM student_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
usernames = cursor.fetchall()

sql_select_Query = "SELECT student_password FROM student_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
passwords = cursor.fetchall()


exam_data =[]
for row in grades: 
	student_list=[]
	student_list.append(row[0])
	student_list.append(row[1])
	student_list.append(row[2])
	student_list.append(row[3])
	student_list.append(row[4])
	exam_data.append(student_list)

username_data =[]
for row in usernames:
	username_data.append(row[0])

password_data =[]
for row in passwords:
	password_data.append(row[0])

print(exam_data)
print(username_data)
print(password_data)



