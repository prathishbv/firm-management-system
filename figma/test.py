from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import register

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x800")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="background.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame_login = Frame()
        frame_login.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_login, width=1600,
                         height=800)

        canvas1.pack(fill="both", expand=True)

        # Display image
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")
        self.username = Entry(frame_login, text="Username1", font=("poppins", 25), bg="#DBFFFA")
        self.username.place(x=650, y=260, width=475, height=52)

        self.password = Entry(frame_login, text="Password1", font=("poppins", 25), bg="#DBFFFA", show="*")
        self.password.place(x=650, y=380, width=475, height=52)


        submit = Button(frame_login, command=self.check_function, text="LOGIN", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=740, y=500, width=291, height=61)
        submit = Button(frame_login, command=self.check_function, text="SIGNUP", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=740, y=650, width=291, height=61)


    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            self.username.destroy()
            self.root.after(2000, register.Register(self.root))

root = Tk()
obj = Login(root)
root.mainloop()