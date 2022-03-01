import Operations
import sys
from tkinter import *
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

    def __init__(self):
        self.base = Tk()
        self.frm = ttk.Frame(self.base, padding=10)
        ttk.Label(self.base, text="What would you like to do?").grid(column=0, row=0)
    
        self.CRUD_frame = ttk.Frame(self.base, padding = 5)

        
        ttk.Button(self.base, text="Select", command=self.base.destroy).grid(column=1, row=0)
        ttk.Button(self.base, text="Quit", command=self.base.destroy).grid(column=2, row=0)

    def run(self):
        self.base.mainloop()

        
