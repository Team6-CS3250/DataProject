from typing import ValuesView
import Operations
import tkinter as tk
from tkinter import *
import tkinter.ttk

db = Operations.Ops('inventory.db')
db.formatTable()

tkwindow = Tk()
tkwindow.geometry('')
tkwindow.title('Team 6 Database Login')
tkwindow['background']='#a9c476'

class frontend_GUI():
    """
    This class will be the front-end of the GUI, where users
    will be able to sign in as employees/customers, and interact with
    the database warehouse, by making orders, checking/update/deleting
    stock, etc.
    """
    def __init__(self, main):
        """ Main sign in page """

        # Welcome label
        self.welcomeLabel = Label(main, text = "WELCOME!",font =("Helvetica",30))
        self.welcomeLabel.grid(row=0, column=3, padx=20, pady=20)
        self.userLabel = Label(main, text = "Select the type of user below:",font=("Helvetica", 15))
        self.userLabel.grid(row=1, column=3)
        self.extraLabel = Label(main, text = "On Time, On Spec, On Budget.", font=("Helvetica", 12))
        self.extraLabel.grid(row=7, column=3, pady=35)

        # Employee and customer button
        self.employeeButton = Button(main, text = "EMPLOYEE",bg='grey',font=("Helvetica",25), command=self.employeeLogin)
        self.employeeButton.grid(row=4, column=2,padx=10, pady=12, ipadx=15, ipady=15)
        self.customerButton = Button(main, text = "CUSTOMER", bg='grey', font=("Helvetica",25))
        self.customerButton.grid(row=4, column=4, padx=10,pady=12, ipadx=15, ipady=15)

    def employeeLogin(self):
        """ Used for the employee button command, displays eployee login page"""

        # Creates second window
        login = Toplevel()
        login.geometry('')
        login.title("Employee Sign In")
        login['background']='#a9c476'

        # Sign in label
        self.signinLabel = Label(login, text = "Sign In", font =("Helvetica",30))
        self.signinLabel.grid(row=0, column=10, pady=15)

        # Line to separate login form
        tkinter.ttk.Separator(login, orient=VERTICAL).grid(column=9, row=0, rowspan=12, sticky='ns', padx=20)

        # Welcome back labels
        self.welcomeLabel = Label(login, text = "Welcome", font =("Helvetica",30))
        self.welcomeLabel.grid(row=1, column=4)
        self.backLabel = Label(login, text = "Back!", font =("Helvetica",30))
        self.backLabel.grid(row=2, column=4)
        self.accLabel = Label(login, text = "Sign into your existing account.", font =("Helvetica",12))
        self.accLabel.grid(row=4, column=4, padx=60)

        # Text entry labels
        self.usernameLabel = Label(login, text = "Username/Email:")
        self.usernameLabel.grid(row=2, column=10, pady=10)
        self.passwordLabel = Label(login, text = "Password:")
        self.passwordLabel.grid(row=4, column=10, pady=10)

        # Text entry
        self.nameEntry = Entry(login, width=20)
        self.nameEntry.grid(row=3, column=10)
        self.passwordEntry = Entry(login, width=20, show='*')
        self.passwordEntry.grid(row=5, column=10, padx=20)

        # Creates button - login & new user
        self.loginButton = Button(login,text = "LOGIN", bg='grey', font=("Helvetica", 15), command=self.navBar)
        self.loginButton.grid(row=6, column=10 ,padx=10, pady=10)
        self.newuserButton = Button(login, text = "New User?", bg='grey', font=("Helvetica", 15),command=self.newUser)
        self.newuserButton.grid(row=6, column=4, pady=10)
    
    def newUser(self):
        """ Creates a new window for new users to create a new account """

        # Creating new window
        self.newWin = Toplevel()
        self.newWin.geometry('250x400')
        self.newWin.title("New User")
        self.newWin.configure(bg='#a9c476')

        # Creating labels
        self.welLabel = Label(self.newWin, text ="Welcome new user!", font =("Helvetica", 20))
        self.welLabel.grid(row=0, column =1, pady=20)
        self.accLabel = Label(self.newWin, text = "New Account", font =("Helvetica", 20))
        self.accLabel.grid(row=1, column =1, pady=20)

        # Creating labels and entries for new account
        self.emailLabel = Label(self.newWin, text="Email:", font =("Helvetica", 15), bg='#a9c476')
        self.emailLabel.grid(row=2, column =1)
        self.emailEntry = Entry(self.newWin, width=20)
        self.emailEntry.grid(row=3, column =0, columnspan=2,padx=20,)

        self.userLabel = Label(self.newWin, text="Username:", font =("Helvetica", 15), bg='#a9c476')
        self.userLabel.grid(row=4, column =1)
        self.userEntry = Entry(self.newWin, width=20)
        self.userEntry.grid(row=5, column =0, columnspan=2,padx=20,)

        self.passLabel = Label(self.newWin, text="Password:", font =("Helvetica", 15), bg='#a9c476')
        self.passLabel.grid(row=6, column =1)
        self.passEntry = Entry(self.newWin, width=20)
        self.passEntry.grid(row=7, column =0, columnspan=2, padx=20)

        # Creating button
        self.createButton = Button(self.newWin, text="Create Account", font=("Helvetica", 15), command=None) #command will store user information
        self.createButton.grid(row=8, column=1, pady=15)

    def navBar(self):
        """ Dashboard Window, where employees will be able to check/update/delete orders """

        self.employee_db = Toplevel()
        self.employee_db.geometry('')
        self.employee_db.title("Employee Dashboard")
        self.employee_db.configure(bg='#a9c476')

        # Dashboard frame
        navFrame=Frame(self.employee_db, width=250, height=550, bg='#a9c476')
        navFrame.place(x=0, y=0)
        #self.dbLabel = Label(self.employee_db, text = "Dashboard",font =("Helvetica",30), bg='#a9c476', height=2, padx=20)
        #self.dbLabel.grid(row=0, column=0, pady=10)


        ''' Creating and Connecting the DB '''

        #Open Database
        self.db = Operations.Ops('inventory.db')

        #Making the frame for the DB table to sit in
        navTableFrame = Frame(self.employee_db, width=250, height=550, bg='#a9c476')
        navTableFrame.grid(row = 0, column = 0, rowspan = 2, columnspan = 5, pady = 10)

        #Creating the format of the table
        cols = list(self.db.viewTable().columns)
        self.tree = tkinter.ttk.Treeview(navTableFrame, columns=cols, show='headings')
        self.tree.heading('date', text='Date')
        self.tree.heading('cust_email', text='Customer Email')
        self.tree.heading('cust_location', text='Customer Location')
        self.tree.heading('product_id', text='Product ID')
        self.tree.heading('product_quantity', text='Units Sold')
        self.tree.heading('trade_number', text='Sale Number')
        self.tree.bind('<Double-1>', self.OnDoubleClick)
        self.tree["columns"] = cols

        #filling the table based on DB
        for i in cols:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor='w')

        for index, row in self.db.viewTable().iterrows():
            self.tree.insert("",0,text=index,values=list(row))
        
        #Inserts tree into its own Grid
        self.tree.grid(row=0, column=0, sticky='nsew')

        #Attaches Scrollbar for DB
        scrollbar = tkinter.ttk.Scrollbar(self.employee_db, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row = 0, column = 5, rowspan = 2, sticky='ns', pady = 10)


        """ Creating buttons for dashboard """

        #Db - product view
        self.dbButton = Button(self.employee_db, text="Refresh", font =("Helvetica", 20), command=lambda: self.dbTableRefresh())
        self.dbButton.grid(row=2, column=0, pady=10, columnspan=1)
        
        #Add products
        self.addButton = Button(self.employee_db, text="Add", font =("Helvetica", 20), command=lambda: [self.db.add(self.addGetValues()), self.dbTableRefresh()])
        self.addButton.grid(row=2, column=1, pady=10, columnspan=1)
        
        #Update products
        self.updateButton = Button(self.employee_db, text="Update", font =("Helvetica", 20), command=lambda: [self.db.edit(self.updateGetValues()), self.dbTableRefresh()])
        self.updateButton.grid(row=2, column=2, pady=10, columnspan=1)
        
        #Delete Products
        self.deleteButton = Button(self.employee_db, text="Delete", font =("Helvetica", 20), command=lambda: [self.db.delete(self.getValues()), self.dbTableRefresh()])
        self.deleteButton.grid(row=2, column=3, pady=10, columnspan=1)

        #Save Products
        self.deleteButton = Button(self.employee_db, text="Save", font =("Helvetica", 20), command=lambda: self.db.saveChanges())
        self.deleteButton.grid(row=2, column=4, pady=10, columnspan=1)

        """ Creating entry feilds """ 
        
        #Product ID label & Entries
        self.prodLabel = Label(self.employee_db, text = "Date")
        self.prodLabel.grid(row=3, column=0, pady=10)
        self.prodEntry = Entry(self.employee_db, width=20)
        self.prodEntry.grid(row=4, column=0, padx=20)

        #Qty Label
        self.qtyLabel = Label(self.employee_db, text = "Customer Email")
        self.qtyLabel.grid(row=3, column=1, pady=10)
        self.qtyEntry = Entry(self.employee_db, width=20)
        self.qtyEntry.grid(row=4, column=1, padx=20)

        #Whole Sale Label
        self.wsLabel = Label(self.employee_db, text = "Location")
        self.wsLabel.grid(row=3, column=2, pady=10)
        self.wsEntry = Entry(self.employee_db, width=20)
        self.wsEntry.grid(row=4, column=2, padx=20)

        #Sale Price Label
        self.spLabel = Label(self.employee_db, text = "Product ID")
        self.spLabel.grid(row=3, column=3, pady=10)
        self.spEntry = Entry(self.employee_db, width=20)
        self.spEntry.grid(row=4, column=3, padx=20)

        #Supplier ID Label
        self.supLabel = Label(self.employee_db, text = "Product Quantity")
        self.supLabel.grid(row=3, column=4, pady=10)
        self.supEntry = Entry(self.employee_db, width=20)
        self.supEntry.grid(row=4, column=4, padx=20, pady= 10)

    def OnDoubleClick(self, event):
        #On double click, fill entryfields with values from selected item
        item = self.tree.selection()

        for i in item:
            #Extract values of the selected item
            prod = str(self.tree.item(i,"values")[0]) 
            qty = str(self.tree.item(i, "values")[1])
            ws = str(self.tree.item(i, "values")[2])
            sp = str(self.tree.item(i, "values")[3])
            sup = str(self.tree.item(i, "values")[4])
            num = str(self.tree.item(i, "values")[5])

            #Clear entry fields
            self.prodEntry.delete(0, END)
            self.qtyEntry.delete(0, END)
            self.wsEntry.delete(0, END)
            self.spEntry.delete(0, END)
            self.supEntry.delete(0, END)

            #Insert the selected value into the entry fields
            self.prodEntry.insert(END, prod)
            self.qtyEntry.insert(END, qty)
            self.wsEntry.insert(END, ws)
            self.spEntry.insert(END, sp)
            self.supEntry.insert(END, sup)

    def dbTableRefresh(self):
        """ Add function to call for changing"""
        self.db = Operations.Ops('inventory.db')
        cols = list(self.db.viewTable().columns)

        #filling the table based on DB
        for i in cols:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor='w')

        for index, row in self.db.viewTable().iterrows():
            self.tree.insert("",0,text=index,values=list(row))

    def updateGetValues(self):
        item = self.tree.selection()
        for i in item:
            num = str(self.tree.item(i, "values")[5])

        prod = self.prodEntry.get()
        qty = self.qtyEntry.get()
        ws = self.wsEntry.get()
        sp = self.spEntry.get()
        sup = self.supEntry.get()

        entry = [prod, qty, ws, sp, sup, num]
        print(entry)
        return entry

    def getValues(self):
        item = self.tree.selection()
        for i in item:
            #Extract values of the selected it
            prod = str(self.tree.item(i,"values")[0]) 
            qty = str(self.tree.item(i, "values")[1])
            ws = str(self.tree.item(i, "values")[2])
            sp = str(self.tree.item(i, "values")[3])
            sup = str(self.tree.item(i, "values")[4])
            num = str(self.tree.item(i, "values")[5])
        
        
        entry = [prod, qty, ws, sp, sup, num]
        print(entry)
        return entry

    def addGetValues(self):
        prod = self.prodEntry.get()
        qty = self.qtyEntry.get()
        ws = self.wsEntry.get()
        sp = self.spEntry.get()
        sup = self.supEntry.get()
        num = 0

        entry = [prod, qty, ws, sp, sup, num]
        print(entry)
        return entry

gui = frontend_GUI(tkwindow)
tkwindow.mainloop()
