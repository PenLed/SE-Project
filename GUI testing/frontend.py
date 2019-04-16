from tkinter import * 
import tkinter.messagebox
import datetime 
from PIL import ImageTk, Image
import os
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

  
def login_verify():
	global username1
	global password1
	username1 = student_username.get()
	password1 = student_password.get()
	
	if username1 in usernames:
		if password1 in passwords:
			login_success()
		else: 
			password_not_recognized()
	else: 
		user_not_found()

def password_not_recognized():
	global pass_error
	pass_error = Toplevel()
	pass_error.geometry("800x600+0+0")
	Label(pass_error, text="Password not recognized").pack()
	Button(pass_error, text="OK", command= delete_password_not_recognised).pack()

def user_not_found():
	global user_not_found
	user_not_found = Toplevel()
	user_not_found.geometry("800x600+0+0")
	Label(user_not_found, text="Username not found").pack()
	Button(user_not_found, text="OK", command=delete_user_not_found_screen).pack()

def delete_password_not_recognised():
	pass_error.destroy()

def delete_user_not_found_screen():
    user_not_found.destroy()

def login_success(): 
	global main_menu
	main_menu = Toplevel()
	main_menu.geometry("800x600+0+0")
	# canvas = Canvas(main_menu, )
	# canvas.pack()
	# img2 = tkinter.PhotoImage(file ='background.jpg')
	# canvas.create_image(100,100, image=img2)
	# path = "background.jpg"
	# #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	# img2 = ImageTk.PhotoImage(Image.open(path))
	# #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	# panel2 = Label(main_menu, image = img2)
	# panel2.pack(side = "bottom", fill = "both", expand = "yes")
	
	mycursor.execute("SELECT student_id FROM student_information WHERE student_username = %s",(username1,))
	student_id = mycursor.fetchall()
	mycursor.execute("SELECT first_name FROM student_information WHERE student_username = %s",(username1,))
	student_fname = mycursor.fetchall()
	mycursor.execute("SELECT last_name FROM student_information WHERE student_username = %s",(username1,))
	student_lname = mycursor.fetchall()
	Label(main_menu, text=("WELCOME!", student_id, student_fname, student_lname), font=("Georgia",30,"bold")).pack()
	


window = Tk()
window.title("Graphical User Interface")
window.geometry('800x600+0+0')
# background_image= PhotoImage(file = "C:\\Users\\Owner\\Desktop\\GUI testing\\main_nackground.jpg")

path = "main_background.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


header = Label(window, text="Learning Management System", font=("Georgia",30,"bold"), fg="black").place(x=120,y=100)
L1 = Label(text="Username", font=("arial",20)).place(x=200, y=200)
L2 = Label(text="Password", font=("arial",20)).place(x=200, y=250)
student_username = Entry(window, bd=5)
student_password = Entry(window, bd=5, show="*")
student_username.place(x=400, y=205)
student_password.place(x=400, y=255)
Button(text="Login", font=("arial", 15), command=login_verify).place(x=400, y=300)
window.mainloop()