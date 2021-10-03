from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# import mysql.connector as mysql
from PIL import ImageTk
import smtplib
from tkinter import scrolledtext
import login




class Status:
    def __init__(self, root):
        self.root = root
        self.root.title("Login page")
        self.root.geometry("1600x850")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="statuspage.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        frame_status = Frame(self.root, bg="white")
        frame_status.place(x=0, y=0, width=1600, height=800)
        canvas1 = Canvas(frame_status, width=1600,
                         height=850)

        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(-50, -50, image=self.bg,
                             anchor="nw")

        submit = Button(frame_status, command=self.salary, text="SALARY DETAILS", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=570, y=550, width=291, height=61)
        submit = Button(frame_status, command=self.update, text="UPDATE STATUS", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=980, y=550, width=291, height=61)
        submit = Button(frame_status, command=self.back, text="BACK", bd=0, font=("poppins", 20, "bold"),
                        bg="#DBFFFA", fg="#40ACB2").place(x=770, y=650, width=291, height=61)

    def salary(self):
        pass

    def update(self):
        pass

    def back(self):
        self.root.after(2000, login.Login(self.root))