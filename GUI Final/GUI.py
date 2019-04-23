
import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image 
from tkinter import * 
from backend import * 
import os 

TITLE = ("Arial", 40, "bold", )
NORMAL_FONT = ("Arial", 20, "bold")
SMALL_FONT = ("Arial", 12)
BG = "white"
FG = "black"

class Window(tk.Tk):# 
    # Initialize everything below
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs) 
       	tk.Tk.iconbitmap(self, "pencil.ico")
        tk.Tk.wm_title(self, "Learning Management System")
        tk.Tk.resizable(self, width=FALSE, height=FALSE)
        tk.Tk.geometry(self, "1280x720")
        # Container that we will populate
        # Frame is basically a window 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, StudentPage, AdminPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self,parent, bg=BG)
    
        
        loginTitle = Label(self, text="WhiteBoard Learn", font=TITLE, bd=4, bg=BG, fg=FG)
        loginTitle.place(rely = .1, relx=.5, anchor="center")
        
        usernameLabel = Label(self, text="USERNAME", font=NORMAL_FONT, bd=4, bg=BG, fg=FG)
        usernameLabel.place(rely = .40, relx=.37, anchor="center")
        

        usernameLabel = Label(self, text="PASSWORD", font=NORMAL_FONT, bd=4, bg=BG, fg=FG)
        usernameLabel.place(rely = .50, relx=.37, anchor="center")
        
        global usernameInput
        usernameInput = Entry(self, bd=4)
        usernameInput.place(rely = .40, relx=.55, anchor="center", width=200, height=30)
        
        global passwordInput
        passwordInput = Entry(self, show="*", bd=4)
        passwordInput.place(rely = .50, relx=.55, anchor="center", width=200, height=30)
        
        loginButton = ttk.Button(self, text="Login", command=lambda:controller.show_frame(StudentPage))
        loginButton.place(rely=.57, relx=.58)

class StudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        label = Label(self, text="My Courses", font=TITLE, bg=BG)
        label.place(relx=.05, rely=.05)
        selected_class = StringVar()
        selected_class.set("Course")

        tree = ttk.Treeview(self, columns = (1,2,3,4,5), height = 10, show = "headings")
        tree.place(relx=0.3, rely=0.3)

        tree.heading(1, text="Class ID")
        tree.heading(2, text="Exam 1")
        tree.heading(3, text="Exam 2")
        tree.heading(4, text="Exam 3")
        tree.heading(5, text= "Final Exam")

        tree.column(1, width = 100)
        tree.column(2, width = 100)
        tree.column(3, width = 100)
        tree.column(4, width = 100)
        tree.column(5, width = 100)

        scroll = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        tree.configure(yscrollcommand=scroll.set)

        for val in exam_data:
            tree.insert('', 'end', values = (val[0], val[1], val[2], val[3], val[4]))

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=TITLE)
        label.pack(pady=10,padx=10)

app = Window()

app.mainloop()

  