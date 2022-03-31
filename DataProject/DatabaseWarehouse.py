from tkinter.messagebox import showinfo
from tkinter.tix import Tree
import Operations
import sys
import tkinter as tk
from tkinter import ttk

class databaseWarehouse():
    """
    This class will be the backend for the GUI, Creating
    the Interface for the Database. Using the methods from
    Operations to use the Database.
    There should be buttons/dropdowns for the following functions:
    - Call (Locate one or multiple IDs, and Search critera.)
    - Add (Ask if you want to save before doing another command)
    - Edit (Ask if you want to save before doing another command)
    - Delete (Ask for comformation)
    - Browse (Shows all IDs in DB)
    - Save Changes (Just commits any changes)
    - Save Copy (Saves any number of selected IDs to another file)
    - Exit (Ask if you want to save if any changes were made)
    """

    def __init__(self, master, **kwargs):
        self.window = tk.Tk()
        self.window.title('Datalog View')

        self.dataFrame = master
        
        cols = list(self.dataFrame.columns)

        tree = ttk.Treeview(self.window, columns=cols, show='headings')
        tree.heading('date', text='Date')
        tree.heading('cust_email', text='Customer Email')
        tree.heading('cust_location', text='Customer Location')
        tree.heading('product_id', text='Product ID')
        tree.heading('product_quantity', text='Units Sold')
        tree["columns"] = cols

        #ttk.Button(tree, text="Select", command=tree.destroy).grid(column=1, row=0)
        #ttk.Button(self.window, text="Quit", command=tree.destroy).grid(column=2, row=0)

        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in self.dataFrame.iterrows():
            tree.insert("",0,text=index,values=list(row))

        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        #scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=tree.yview)
        #tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(row=0, column=1, sticky='ns')

        #self.create_text()
        #dataBase = Operations.Ops('inventory.db')
        
        #self.tree = ttk.Treeview(self.base, colum="date", "cust_email", "cust_location", "product_id", "product_quantity", show="headings")

        #ttk.Label(self.base, text="What would you like to do?").grid(column=0, row=0)
    
        #self.CRUD_frame = ttk.Frame(self.base, padding = 5)

        
        #ttk.Button(self.base, text="Select", command=self.base.destroy).grid(column=1, row=0)
        #ttk.Button(self.base, text="Quit", command=self.base.destroy).grid(column=2, row=0)
    def item_selected(event):
        for selected_item in Tree.selection():
            item = ttk.Treeview.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
    
        
    def run(self):
        self.window.mainloop()

        
