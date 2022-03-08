# This is not a neccessary class, but the methods within can fill
# in the gaps elsewhere in the project where these operations are necessary.
from dataclasses import dataclass
import sqlite3
import pandas as pd
import Operations
from sqlite3 import Error

class CRUD_operations(Operations):

    # Connect to the sqlite database
    dataBase = sqlite3.connect('db_File')
    # cursor object
    cur = dataBase.cursor()
    # Drop query
    cur.execute("DROP TABLE IF EXISTS ENTRY")

    def create(database, entry):
    # This function calls functions from the operations 
    # class to perform the desired create function
        
        # !! Is it necessary to wrap this all in an if else?
        # Determine if database is empty or not and proceed thusly
        # we still have to get his figured out
        if database == None:
            # create query
            query = """CREATE TABLE INVENTORY(PRODUCT_ID CHAR(12) PRIMARY KEY NOT NULL,
                    QUANTITY INT, WHOLESALE_COST REAL, 
                    SALE_PRICE REAL, SUPPLIER_ID CHAR(8) )"""
            dataBase.execute(query)

            # commit and close
            dataBase.commit()
            dataBase.close()
            
        else:
            # Drop query
            query = ('INSERT INTO INVENTORY(PRODUCT_ID, QUANTITY, WHOLESALE_COST, SALE_PRICE, SUPPLIER_ID' 
                    'VALUES (:PRODUCT_ID, :QUANTITY, :WHOLESALE_COST, :SALE_PRICE, :SUPPLIER_ID);')
            
            # Will need to connect this to GUI to take in new entry
            newEntry = {}
            dataBase.execute(query, newEntry)
            dataBase.commit()
            database.close()
           


    def read():
    # This functions calls functions from the operations 
    # class to perform the desired read function
<<<<<<< HEAD
        cur = dataBase.execute("SELECT * from INVENTORY")
        
        # Temporarily will print inventory to terminal
        # **will need to change to interact with GUI**
        print(cur.fetchall())

        # Will need to add read selected entries

        dataBase.close()

=======
        pass
>>>>>>> master

    def update():
    # This function calls functions from the operations
    # class to perform the desired update function
<<<<<<< HEAD
    # This will involve (1) reaching the entry and (2) the changing it

        dataBase.exectue("UPDATE INVNETORY set ROLL = 005 where ID = 1")
        dataBase.commit()

        cur = dataBase.execute("SELECT * from INVENTORY")
        
        # Print to ensure change
        print(cur.fetchall())

        dataBase.close()
=======
        pass
>>>>>>> master

    def delete():
    # This function calls functions from teh operations
    # class to perform the desired delete function
<<<<<<< HEAD

        dataBase.execute("DELETE from INVENTORY where ID = 2;")
        dataBase.commit()

        cur = dataBase.execute("SELECET * from INVENTORY")
        print(cur.fetchall())

        dataBase.close()
=======
        pass
>>>>>>> master
