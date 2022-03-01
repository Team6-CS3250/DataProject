import sqlite3
from sqlite3 import Error

class CRUD_operations():

    def create(database, entry):
    # This function calls functions from the operations 
    # class to perform the desired create function
        
        # Determine if database is empty or not and proceed thusly
        if database == None:
            # Drop Query
            query = "Create new database?"

            # connect to database and create new table
            try:
                c = database.cursor()
                c.execute(query)
            except Error as e:
                print(e)
        
            return database
        else:
            # Drop query
            query = ''' INSERT INTO entries() VALUES(?, ?, ?, ?, ?)'''
            cur = database.cursor()
            cur.execute(query, entry)
            database.commit()
            return cur.lastrowid 


    def read():
    # This functions calls functions from the operations 
    # class to perform the desired read function


    def update():
    # This function calls functions from the operations
    # class to perform the desired update function

    def delete():
    # This function calls functions from teh operations
    # class to perform the desired delete function
