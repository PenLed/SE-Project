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
exam1 = []
exam2 = []
exam3 = []
final_exam = []
for row in grades: 
	class_id.append(row[0])
	exam1.append(row[1])
	exam2.append(row[2])
	exam3.append(row[3])
	final_exam.append(row[4])
print (class_id) 
print (exam1)
print (exam2) 
print (exam3)
print (final_exam)