import tkinter as tk
from tkinter import *
import tkinter.messagebox
import random
from PIL import ImageTk, Image


window = tk.Tk()
window.geometry("500x510+380+100")
window.resizable(width=0, height=0)
window.title("Love Calculator by me")
window.configure(bg='pink')

path = "love2.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.place(x = 0 , y = 0)


user1 = tk.StringVar()
user2 = tk.StringVar()

def submit():
    fName = user1.get()
    sName = user2.get()

    print("The name is : " + fName)
    print("The her name is : " + sName)

    user1.set("")
    user2.set("")
    hello()

def hello():
    a = random.randrange(1, 100)
    b = a,"%"
    print("Your love percentage is", a , "%")
    tkinter.messagebox.showinfo("%",b)


fName_label = Label(window,text="Enter your name",font=('Arial,20'),fg='blue',bg='white',relief="sunken",border=6)



fName_entry = tk.Entry(window,textvariable=user1, font=('calibre',10,'normal'),relief="groove",border=5)


sName_label = Label(window,text="Enter her name",font=('Arial,20'),fg='blue',bg='white',relief="sunken",border=6)


sName_entry=tk.Entry(window, textvariable=user2, font=('calibre',10,'normal'),relief="groove",border=5)


cal_btn=tk.Button(window,text = 'Calculate', command = submit,relief="ridge",border=6,fg='green',bg='white',font='bold')


fName_label.grid(column=0,row=1,padx=12,pady=9)
fName_entry.grid(column=0,row=2,padx=12,pady=7)

sName_label.grid(column=0,row=3,padx=12,pady=9)
sName_entry.grid(column=0,row=4,padx=12,pady=9)

cal_btn.grid(column=1,row=5,pady=55,padx=24)


window.mainloop()

