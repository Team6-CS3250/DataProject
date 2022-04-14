#password and username entry field
#needs to be debugged and tested

from cProfile import label
from tkinter import PhotoImage, Tk
from tkinter import font
from tkinter.font import Font
from tkinter import *
import sys

def command1(even):
    if entry1.get() == 'admin' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconfy()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()
root = Tk()
top = Toplevel()
top.geometry('300x260')
top.title('LOGIN SCREEN') 
top.configure(background='white')
photo2 = PhotoImage(file='1.gif')
photo = Label(top, image=photo2, bg='white')
lbl1 = Label(top, text='username:',font=('Helvetica',10))
entry1 = Entry(top)
lbl2 = Label(top, text='password:',font=('Helvetica', 10))
entry2 = Entry(top, show="*")
button2 = Button(top, text='Cancel', command=lambda:command2())

entry2.bind('<Return>',command1)

lbl3 = Label(top, tect='Copyright login Screen 2022',font=('Arial',9))

photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

root.tile('Main Screen')
root.configure(backround= 'white')
root.geometry('855x650')

root.withdraw()
root.mainloop()