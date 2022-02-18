import sqlite3

class operations():
    """ 
    The Operations File containes all of the operator classes to interact with
    the data in the Database, with callable functions for the Gui to use.
    """

    def __init__(self, database):
    # On call from GUI, this initaits by connecting to the DB.
        database = sqlite3.connect("")
        current = database.cursor()

        return

    def saveChanges(self):
    # On call asks if you would like to save changes, editiing the table.
        database.commit()

    def find(self):
    # This function is used to find an ID from the DB.
     
        return

    def view(self, ID_Number):
    # This function is used to return the ID given to it.

        return

    def add(self):
    # This function adds a new ID to the DB.

        return

    def edit(self):
    # This function edits the ID that is recived.

        return

    def delete(self):
    # This function deletes the ID currently being recived.
    
        return

    def exit(self):
    # This function will close out of the DB.
        database.close()
