from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as ms
import mysql.connector as mysql
from tkinter import ttk
import tkinter as tk
from subprocess import call

win =Tk()
win.geometry("1280x700+0+0")
win.resizable(0,0)
v1=IntVar()
win.title("Sign Up page")


def signup():
      if len(t2.get()) == 0:
            ms.showerror('Error', 'Please Enter Username')
            t2.focus_set()
      elif len(t3.get()) == 0:
            ms.showerror("Error", "please Enter Your Email")
            t3.focus_set()
      elif len(t4.get()) == 0:
            ms.showerror("Error", "Please Enter Your Password")
            t4.focus_set()

      elif len(t5.get()) == 0:
            ms.showerror("Error", "please Enter Your Password")
            t5.focus_set()

      else:

            con = mysql.connect(user="root", password="", host="localhost", database='login_cred')
            cur = con.cursor()
            username = t2.get();
            email = t3.get();
            password = t4.get();
            confirmpassword = t5.get();

            sql = "insert into credential values(%s,%s,%s,%s)";
            val = (username, email, password, confirmpassword)
            cur.execute(sql, val)
            con.commit()
            ms.showinfo("Success", "Registration Successful")


def reset():
      t2.delete(0, END)
      t3.delete(0, END)
      t4.delete(0, END)
      t5.delete(0, END)


def back():
      win.destroy()
      call(["python", "login.py"])


bgImg=ImageTk.PhotoImage(file="Pri_Regd_bg.jpg")
l1=Label(win,image=bgImg)
l1.place(x=0,y=0)

f1=Frame(win,bg="#0074B7",width=560,height=490)
f1.place(x=360,y=150)

l=Label(f1,text="SIGN UP",fg="DodgerBlue4",bg="light blue",font=("Times new roman",40,"bold"),width=21)
l.place(x=0,y=0)

l2=Label(f1,text="Username:",font=("Times new roman",18,"bold"),bg="#0074B7",fg="white")
l2.place(x=30,y=80)
t2=Entry(f1,font=("Times new roman",16),bd=1,width=30,bg="#D4F1F4")    #username
t2.place(x=30,y=110)

l3=Label(f1,text="Email:",font=("Times new roman",18,"bold"),bg="#0074B7",fg="white")
l3.place(x=30,y=150)
t3=Entry(f1,font=("Times new roman",16),bd=1,width=30,bg="#D4F1F4")    #email
t3.place(x=30,y=180)

l4=Label(f1,text="Password:",font=("Times new roman",18,"bold"),bg="#0074B7",fg="white")
l4.place(x=30,y=230)
t4=Entry(f1,font=("Times new roman",16),bd=1,width=30,bg="#D4F1F4",show="*")    #password
t4.place(x=30,y=260)

l5=Label(f1,text="Confirm Password:",font=("Times new roman",18,"bold"),bg="#0074B7",fg="white")
l5.place(x=30,y=310)
t5=Entry(f1,font=("Times new roman",16),bd=1,width=30,bg="#D4F1F4",show="*")    #confirm password
t5.place(x=30,y=340)


b1=Button(f1,text="Sign Up",bg="lime green",width=10,
      font=("Times new Roman",16,"bold"),activebackground="lime green",bd=0,cursor="hand2", command=signup)
b1.place(x=150,y=390)
b2=Button(f1,text="Reset",font=("Times new roman",16,"bold"),activebackground="#D4F1F4",
      cursor="hand2",bg="#D4F1F4",bd=0,width=8,command=reset )
b2.place(x=300,y=390)
b3=Button(f1,text="Back to login page",bg="#EEEDE7",fg="blue",bd=1,width=15, font=("Times new Roman",13,"bold"),
          activebackground="#EEEDE7",cursor="hand2",command=back)
b3.place(x=380,y=450)



win.mainloop()