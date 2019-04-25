#-----------------------ESTABLISHING CONNECTION-------------------------------

import mysql.connector

mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "Catharsys@1993",
			database="lms"
	)

cursor = mydb.cursor()

def get_student_details(ID):
    sql_select_query = """select * from student_information where student_id = %s"""
    cursor.execute(sql_select_query, (ID, ))
    record = cursor.fetchall()
    for row in record:
     print("Student Name = ", row[0], )
     print("Username  = ", row[1], "\n")

def retrieve_input():
    input_value = textbox.get("1.0", "end-1c")
    get_student_details(input_value)

#-----------------------------------GRADES-----------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT  * FROM class_grade WHERE student_id = '1' "
cursor.execute(sql_select_Query)
grades = cursor.fetchall()

exam_data =[]
for row in grades: 
	student_list=[]
	student_list.append(row[0])
	student_list.append(row[1])
	student_list.append(row[2])
	student_list.append(row[3])
	student_list.append(row[4])
	exam_data.append(student_list)

#-----------------------------------USERNAMES-------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT student_username FROM student_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
usernames = cursor.fetchall()
#LIST
username_data =[]
for row in usernames:
	username_data.append(row[0])
#----------------------------------PASWORDS---------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT student_password FROM student_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
passwords = cursor.fetchall()
#LIST
password_data =[]
for row in passwords:
	password_data.append(row[0])

#-------------------------------STUDENT INFO--------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT student_id, student_name FROM student_information"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
student_info = cursor.fetchall()
#LIST
student_data =[]
for row in student_info: 
	students=[]
	students.append(row[0])
	students.append(row[1])
	student_data.append(students)

#--------------------------------ADMIN USERNAMES-------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT admin_username FROM admin_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
usernames = cursor.fetchall()
#LIST
admin_username_data =[]
for row in usernames:
	admin_username_data.append(row[0])
#---------------------------------ADMIN PASWORDS---------------------------------
#SQL STATMENTS
sql_select_Query = "SELECT admin_password FROM admin_login"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
admin_passwords = cursor.fetchall()
#LIST
admin_password_data =[]
for row in admin_passwords:
	admin_password_data.append(row[0])

print(grades) 