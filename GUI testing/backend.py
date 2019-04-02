import sqlite3 

def login():
	for i in range(3):
		while True: 
			username = input("Username: ")
			password = input("Password: ")