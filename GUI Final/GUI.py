
import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image 
from tkinter import * 
from backend import * 

TITLE = ("Arial", 40, "bold", "underline")
NORMAL_FONT = ("Arial", 20, "bold")
SMALL_FONT = ("Arial", 12)
BG = "light grey"
FG = "black"

# Defining our class Window
# Inheritance in paranthesis, in this case from tk.Tk 
class Window(tk.Tk):# 
    # Initialize everything below
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs) 
       	tk.Tk.iconbitmap(self, default="pencil.ico")
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

def login_verify(): 
    print("You did it!")
        
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        # background=tk.PhotoImage("background.png")
        tk.Frame.__init__(self,parent, bg=BG)
        
        loginTitle = Label(self, text="WhiteBoard Learn", font=TITLE, bd=4, bg=BG, fg=FG)
        loginTitle.place(rely = .1, relx=.5, anchor="center")
        
        usernameLabel = Label(self, text="USERNAME", font=NORMAL_FONT, bd=4, bg=BG, fg=FG)
        usernameLabel.place(rely = .40, relx=.37, anchor="center")
        
        usernameLabel = Label(self, text="PASSWORD", font=NORMAL_FONT, bd=4, bg=BG, fg=FG)
        usernameLabel.place(rely = .50, relx=.37, anchor="center")
        
    
        usernameInput = Entry(self, bd=4)
        usernameInput.place(rely = .40, relx=.55, anchor="center", width=200, height=30)
        
        passwordInput = Entry(self, show="*", bd=4)
        passwordInput.place(rely = .50, relx=.55, anchor="center", width=200, height=30)
        
        loginButton = Button(self, text="Login", font=SMALL_FONT, command=lambda:controller.show_frame(StudentPage))
        loginButton.place(rely=.57, relx=.58)

class StudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        label = Label(self, text="My Courses", font=TITLE, bg=BG)
        label.place(relx=.05, rely=.05)
        selected_class = StringVar()
        selected_class.set("Course")
        class_menu = OptionMenu(self, selected_class, *class_id)
        class_menu.config(height=2, width = 20)
        class_menu.place(relx=.05, rely=.2)

        tree = ttk.Treeview(self)
        tree["columns"]=("one","two","three")
        tree.column("#0", width=200, minwidth=200, stretch=tk.NO)
        tree.column("one", width=200, minwidth=200, stretch=tk.NO)
        tree.column("two", width=200, minwidth=200)
        tree.column("three", width=200, minwidth=200, stretch=tk.NO)

        tree.heading("#0",text="Exam 1",anchor=tk.W)
        tree.heading("one", text="Exam 2",anchor=tk.W)
        tree.heading("two", text="Exam 3",anchor=tk.W)
        tree.heading("three", text="Final Exam",anchor=tk.W)
        tree.place(relx=.2, rely=.25)

        
class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=TITLE)
        label.pack(pady=10,padx=10)

app = Window()

app.mainloop()

  