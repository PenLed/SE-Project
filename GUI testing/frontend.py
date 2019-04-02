from tkinter import * 
from backend import * 
import tkinter.messagebox
import datetime 
from PIL import ImageTk, Image
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


header = Label(window, text="Learning Management System", font=("arial",30,"bold"), fg="black", bg="SlateGray1").place(x=120,y=100)
L1 = Label(text="Username", font=("arial",20)).place(x=200, y=200)
L2 = Label(text="Password", font=("arial",20)).place(x=200, y=250)
student_username = Entry(window, bd=5)
student_password = Entry(window, bd=5)
student_username.place(x=400, y=205)
student_password.place(x=400, y=255)

window.mainloop()