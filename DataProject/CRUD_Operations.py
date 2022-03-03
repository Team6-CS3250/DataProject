# This is not a neccessary class, but the methods within can fill
# in the gaps elsewhere in the project where these operations are necessary.
import sqlite3
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
        if database == None:
            # create query
            query = """CREATE TABLE ENTRY(PRODUCT_ID CHAR(12) PRIMARY KEY NOT NULL,
                    QUANTITY INT, WHOLESALE_COST REAL, 
                    SALE_PRICE REAL, SUPPLIER_ID CHAR(8) )"""
            dataBase.execute(query)

            # commit and close
            dataBase.commit()
            dataBase.close()
            
        else:
            # Drop query
            query = ('INSERT INTO ENTRY(PRODUCT_ID, QUANTITY, WHOLESALE_COST, SALE_PRICE, SUPPLIER_ID' 
                    'VALUES (:PRODUCT_ID, :QUANTITY, :WHOLESALE_COST, :SALE_PRICE, :SUPPLIER_ID);')
            
            # Will need to connect this to GUI to take in new entry
            newEntry = {}
            dataBase.execute(query, newEntry)
            dataBase.commit()
            database.close()
           


    def read():
    # This functions calls functions from the operations 
    # class to perform the desired read function


    def update():
    # This function calls functions from the operations
    # class to perform the desired update function

    def delete():
    # This function calls functions from teh operations
    # class to perform the desired delete function
