import Operations
import tkinter as tk
from tkinter import *
import tkinter.ttk

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
        self.newuserButton = Button(login, text = "New User?", bg='grey', font=("Helvetica", 15))
        self.newuserButton.grid(row=6, column=4, pady=10)

    def navBar(self):
        """ Dashboard Window, where employees will be able to check/update/delete orders """

        self.employee_db = Toplevel()
        self.employee_db.geometry('')
        self.employee_db.title("Employee Dashboard")
        self.employee_db.configure(bg='#a9c476')

        # Dashboard frame
        navFrame=Frame(self.employee_db, width=250, height=550, bg='#a9c476')
        navFrame.place(x=0, y=0)
        self.dbLabel = Label(self.employee_db, text = "Dashboard",font =("Helvetica",30), bg='#a9c476', height=2, padx=20)
        self.dbLabel.grid(row=0, column=0, pady=10)

        """ Creating buttons for dashboard """

        #Db - product view
        self.dbButton = Button(self.employee_db, text="Database", font =("Helvetica", 20), command=self.navTable)
        self.dbButton.grid(row=1, column=0, pady=15, columnspan=1)
        
        #New orders
        self.orderButton = Button(self.employee_db, text="New Orders", font =("Helvetica", 20), command=None)
        self.orderButton.grid(row=2, column=0, pady=15, columnspan=1)
        
        #Add products
        self.addButton = Button(self.employee_db, text="Add", font =("Helvetica", 20), command=self.navAdd)
        self.addButton.grid(row=3, column=0, pady=15, columnspan=1)
        
        #Update products
        self.updateButton = Button(self.employee_db, text="Update", font =("Helvetica", 20), command=None)
        self.updateButton.grid(row=4, column=0, pady=15, columnspan=1)
        
        #Delete Products
        self.deleteButton = Button(self.employee_db, text="Delete", font =("Helvetica", 20), command=self.navDelete)
        self.deleteButton.grid(row=5, column=0, pady=15, columnspan=1)

    def navTable(self):
        """ On button push, bring up the db table on the table."""

        #Open Database
        self.db = Operations.Ops('inventory.db')

        #Make the sperater from table to sidebar
        tkinter.ttk.Separator(self.employee_db, orient=VERTICAL).grid(column=1, row=0, rowspan=6, sticky='ns', padx=20)

        #Making the frame for the DB table to sit in
        navTableFrame = Frame(self.employee_db, width=250, height=550, bg='#a9c476')
        navTableFrame.grid(row = 0, column = 2, rowspan = 2, columnspan = 3, pady = 10)

        #Creating the format of the table
        cols = list(self.db.viewTable().columns)
        tree = tkinter.ttk.Treeview(navTableFrame, columns=cols, show='headings')
        tree.heading('date', text='Date')
        tree.heading('cust_email', text='Customer Email')
        tree.heading('cust_location', text='Customer Location')
        tree.heading('product_id', text='Product ID')
        tree.heading('product_quantity', text='Units Sold')
        tree["columns"] = cols

        #filling the table based on DB
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in self.db.viewTable().iterrows():
            tree.insert("",0,text=index,values=list(row))
        
        #Inserts tree into its own Grid
        tree.grid(row=0, column=0, sticky='nsew')

        #Attaches Scrollbar for DB
        scrollbar = tkinter.ttk.Scrollbar(self.employee_db, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row = 0, column = 5, rowspan = 2, sticky='ns', pady = 10)
    
    def getValues(self):
        prod = self.prodEntry.get()
        qty = self.qtyEntry.get()
        ws = self.wsEntry.get()
        sp = self.spEntry.get()
        sup = self.supEntry.get()
        
        entry = (prod, qty, ws, sp, sup)
        print(entry)
        return entry





    def navAdd(self):
        """ On button push, props up new screen to add products """

        #Creating new window
        self.addWin = Toplevel()
        self.addWin.geometry('')
        self.addWin.title("Add Products")
        self.addWin.configure(bg='white')

        self.addLabel = Label(self.addWin, text = "Add Product:", font =("Helvetica", 20))
        self.addLabel.grid(row=0, column=0, pady=10)

        #Product ID label & Entries
        self.prodLabel = Label(self.addWin, text = "Date:")
        self.prodLabel.grid(row=1, column=0, pady=10)
        self.prodEntry = Entry(self.addWin, width=20)
        self.prodEntry.grid(row=1, column=1, padx=20)

        #Qty Label
        self.qtyLabel = Label(self.addWin, text = "Customer Email:")
        self.qtyLabel.grid(row=2, column=0, pady=10)
        self.qtyEntry = Entry(self.addWin, width=20)
        self.qtyEntry.grid(row=2, column=1, padx=20)

        #Whole Sale Label
        self.wsLabel = Label(self.addWin, text = "Location:")
        self.wsLabel.grid(row=3, column=0, pady=10)
        self.wsEntry = Entry(self.addWin, width=20)
        self.wsEntry.grid(row=3, column=1, padx=20)

        #Sale Price Label
        self.spLabel = Label(self.addWin, text = "Product ID:")
        self.spLabel.grid(row=4, column=0, pady=10)
        self.spEntry = Entry(self.addWin, width=20)
        self.spEntry.grid(row=4, column=1, padx=20)

        #Supplier ID Label
        self.supLabel = Label(self.addWin, text = "Product Quantity:")
        self.supLabel.grid(row=5, column=0, pady=10)
        self.supEntry = Entry(self.addWin, width=20)
        self.supEntry.grid(row=5, column=1, padx=20)

        #Add Button
        self.addButton = Button(self.addWin, text = "Add Product")
        self.addButton.grid(row=6, column=1, columnspan=2, command = self.db.add(self.getValues()) ) #command will add product to db

    def navDelete(self):
        """ On button push, props up new screen to delete products """

        #Creating new window
        self.deleteWin = Toplevel()
        self.deleteWin.geometry('')
        self.deleteWin.title("Delete Products")
        self.deleteWin.configure(bg='white')

        self.deleteLabel = Label(self.deleteWin, text = "Delete Product:", font =("Helvetica", 20))
        self.deleteLabel.grid(row=0, column=0, pady=10)

        #Product ID label & Entries
        self.prodLabel = Label(self.deleteWin, text = "Product ID:")
        self.prodLabel.grid(row=1, column=0, pady=10)
        self.prodEntry = Entry(self.deleteWin, width=20)
        self.prodEntry.grid(row=1, column=1, padx=20)

        #Qty Label
        self.qtyLabel = Label(self.deleteWin, text = "Qty:")
        self.qtyLabel.grid(row=2, column=0, pady=10)
        self.qtyEntry = Entry(self.deleteWin, width=20)
        self.qtyEntry.grid(row=2, column=1, padx=20)

        #Whole Sale Label
        self.wsLabel = Label(self.deleteWin, text = "Whole Sale:")
        self.wsLabel.grid(row=3, column=0, pady=10)
        self.wsEntry = Entry(self.deleteWin, width=20)
        self.wsEntry.grid(row=3, column=1, padx=20)

        #Sale Price Label
        self.spLabel = Label(self.deleteWin, text = "Sale Price:")
        self.spLabel.grid(row=4, column=0, pady=10)
        self.spEntry = Entry(self.deleteWin, width=20)
        self.spEntry.grid(row=4, column=1, padx=20)

        #Supplier ID Label
        self.supLabel = Label(self.deleteWin, text = "Supplier ID:")
        self.supLabel.grid(row=5, column=0, pady=10)
        self.supEntry = Entry(self.deleteWin, width=20)
        self.supEntry.grid(row=5, column=1, padx=20)

        #Delete Button
        self.addButton = Button(self.deleteWin, text = "Delete Product")
        self.addButton.grid(row=6, column=1, columnspan=2, command=Operations.delete) #command will delete product from db


gui = frontend_GUI(tkwindow)
tkwindow.mainloop()
