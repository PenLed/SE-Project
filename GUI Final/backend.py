import mysql.connector
from mysql.connector import Error 
mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "Catharsys@1993",
			database="lms"
	)

sql_select_Query = "SELECT  * FROM class_grade WHERE student_id = '1' "
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
grades = cursor.fetchall()
class_id = []

for row in grades: 
	class_id.append(row[0])
	print("Class: ", row[0])
	print("Exam 1: ", row[1])
	print("Exam 2: ", row[2])
	print("Exam 3: ", row[3])	
	print("Final Exam: ", row[4])
	
print (class_id) 