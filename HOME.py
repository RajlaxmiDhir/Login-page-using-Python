from tkinter import *
from tkinter import ttk,messagebox
from subprocess import call
from PIL import ImageTk


win =Tk()
win.geometry("1280x700+0+0")
win.resizable(0,0)
win.title("Dashboard")


bgImg=ImageTk.PhotoImage(file="home_bg.jpg")
l1=Label(win,image=bgImg)
l1.place(x=0,y=0)

l=Label(win,text=" USER DASHBOARD ",bg="#C55FFC",fg="WHITE",font=("Castellar",52,"bold"))
l.place(x=200,y=150)

b1=Button(win,text="GIT HUB PROFILE",font=("Times new Roman",22,"bold"),
          bg='#EFDCF9',fg='#341948',bd=5, width=25,
          activebackground="#EFDCF9",activeforeground="#341948",cursor="hand2")
b1.place(x=250,y=300)

b2=Button(win,text="UPDATE YOUR INFO",font=("Times new Roman",22,"bold"),
          bg='#EFDCF9', fg='#341948', bd=5, width=25,
          activebackground="#EFDCF9", activeforeground="#341948", cursor="hand2")
b2.place(x=730,y=300)

b3=Button(win,text="CHANGE PASSWORD",font=("Times new Roman",22,"bold"),
          bg='#EFDCF9', fg='#341948', bd=5, width=25,
          activebackground="#EFDCF9", activeforeground="#341948", cursor="hand2")
b3.place(x=500,y=400)


b7=Button(win,text="LOG OUT",font=("Times new Roman",20,"bold"),
          bg='#EFDCF9', fg='#341948', bd=5, width=8,
          activebackground="#EFDCF9", activeforeground="#341948", cursor="hand2")
b7.place(x=910,y=550)

b8=Button(win,text="<===",bg="red",bd=6,font=18)
b8.place(x=1200,y=620)



win.mainloop()


