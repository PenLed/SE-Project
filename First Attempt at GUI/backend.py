import sqlite3 

def connect():
	conn=sqlite3.connect("student.db")
	cur=conn.cursor() 
	cur.execute("CREATE TABLE IF NOT EXIST student (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone_number INTEGER, major TEXT)")
	conn.commit()
	conn.close() 

def insert(name, address, phone_number, major): 
	conn=sqlite3.connect("students.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO student VALUE (NULL, ?, ?, ?, ?)"(name, address, phone_number, major))
	conn.commit()
	conn.close()
	view() 

def view():
	conn=sqlite3.connect("students.db")
	cur=conn.cursor() 
	cur.execute("SELECT * FROM student")
	row=cur.fetchall()
	conn.close()
	return rows 