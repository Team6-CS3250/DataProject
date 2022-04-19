#I have started to make a password bank. This is what i have so far.


import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Bank")

def loginScreen():
    window.geometry("350x150")

    lbl = Label(window, text = "Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window)
    lbl1.pack()

    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    def checkPassword():
        password = "test"

        if password == txt.get():
            print("Right password")
        else:
            lbl1.config(text="wrong Password")




    btn = Button(window, text="submit" , command=checkPassword)
    btn.pack(pady=10)



loginScreen()
window.mainloop()







