from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb
from subprocess import call
import mysql.connector as mysql

win = Tk()
win.geometry("1280x700+25+0")
win.resizable(0, 0)
win.title("Login Page")


def login():
    if len(t3.get()) == 0:

        mb.showinfo("warning", "Username  is blank please enter")
        t3.focus_set()

    elif len(t4.get()) == 0:
        mb.showinfo("warning", "password is blank please enter")
        t4.focus_set()
    else:

        username = t3.get();

        password = t4.get();
        conn = mysql.connect(user='root', password='', host='localhost', database='login_cred')
        cur = conn.cursor()
        sql = "select * from credential where username=%s and password=%s "
        cur.execute(sql, [(username), (password)])

        results = cur.fetchall()
        conn.commit()

        if results:

            win.destroy()

            call(["python", "HOME.py"])
        else:
            mb.showinfo("", "Login failed")


def reg():
    win.destroy()
    call(["python", "regd.py"])


bgImg = ImageTk.PhotoImage(file="PriLogin_bg.jpg")
l1 = Label(win, image=bgImg)
l1.place(x=0, y=0)

f1 = Frame(win, bg="#68BBE3")
f1.place(x=700, y=100)

logo = PhotoImage(file="PriLogo.png")
l2 = Label(f1, image=logo, bg="#68BBE3")
l2.grid(row=0, column=0, columnspan=4, pady=10)

user = PhotoImage(file="PriUser.png")
l3 = Label(f1, image=user, text="username", compound=LEFT, font=("Times new Roman", 18, "bold"),
           bg="#68BBE3", fg="white")
l3.grid(row=1, column=0, pady=10, padx=20)

t3 = Entry(f1, font=("Times new Roman", 16, "bold"), bd=1, fg="midnight blue")
t3.grid(row=1, column=1)

password = PhotoImage(file="PriPass.png")
l4 = Label(f1, image=password, text="Password", compound=LEFT, font=("Times new Roman", 18, "bold"),
           bg="#68BBE3", fg="white")
l4.grid(row=2, column=0, pady=10, padx=20)

t4 = Entry(f1, font=("Times new Roman", 16, "bold"), bd=1, fg="midnight blue", show="*")
t4.grid(row=2, column=1, )

b4 = Button(f1, text="Forgot Password ?", font=("Times new Roman", 11, "bold"), width=15, bg="#68BBE3",
            fg="white", bd=0, activebackground="#68BBE3", activeforeground="#BFD7ED")
b4.grid(row=3, column=1, columnspan=5)

b1 = Button(f1, text="Login", font=("Times new Roman", 14, "bold"), width=15, bg="lime green",
            activebackground="lime green",
            bd=0, cursor="hand2", command=login)
b1.grid(row=4, column=0, columnspan=4, pady=10)

l5 = Label(f1, text="Are you a new user ? click here ->", font=("Times new Roman", 16, "bold"), bg="#68BBE3",
           fg="white")
l5.grid(row=5, column=0, columnspan=2, pady=10)

b2 = Button(f1, text="Sign Up", font=("Times new Roman", 14, "bold underline"), bg="#68BBE3",
            fg="#003060", bd=0, activebackground="#68BBE3", activeforeground="#7EC8E3", cursor="hand2", command=reg)
b2.grid(row=5, column=2)

win.mainloop()