import sqlite3
from sqlite3 import Error
from this import d

from frontend_GUI import filename
from frontend_GUI import user_addition
from frontend_GUI import user_update
from frontend_GUI import user_deletion
import pandas as pd


class Ops():
    """ 
    The Operations File containes all of the operator classes to interact with
    the data in the Database, with callable functions for the Gui to use.
    """
    

    def __init__(self, db_file):
        """ On call from GUI, this initaits by connecting to the DB. """

        #  In addition to accessing the customer_orders.db, is it not important to 
        # also include the inventory.db in all these operations
        
        # connects to frontend to retrieve user requested file
        db_file = filename
        con = None
        try: #Trying to connect to the given DB file path.
            self.database = sqlite3.connect(db_file)
            print(sqlite3.version)
            self.cur = self.database.cursor()

        except Error as e: #Returns the error type, if the DB was unable to be connected to.
            print(e)

        finally: #Closes the DB if an Error occures.
            if con:
                con.close()


    def formatTable(self):
        """Fixer method that is to format the table, use only if the table is not in the DB. """
        
        csv_file_name = 'customer_orders_team6.csv' # will be 'filename'
        data = pd.read_csv(csv_file_name)
        df = pd.DataFrame(data)
        cur = self.database.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS customer_orders(date TEXT, cust_email TEXT, cust_location INTEGER, product_id TEXT, product_quantity INTEGER)")
        data.to_sql('customer_orders', self.database, if_exists='replace', index=False)
        self.database.commit()


    def viewTable(self):
        """ Converts DB to readable table then returns it. """

        cur = self.database.cursor()
        con = self.database        
        cur.execute("SELECT * FROM customer_orders")
        df = pd.read_sql_query("SELECT * from customer_orders", con)
        return(df)


    def saveChanges(self):
        """ When called it saves any changes that were made to the DB."""

        self.database.commit()

    #  Do we want to just "assertTrue" whether the ID exists in the file? 
    # or do we want to return the entire entry? (Though this operation is completed
    # in the find function)
    # or view the whole table?
    def view(self):
        """ This function is used to find an ID from the DB. """
        
        return


    def find(self, key, entry):
        """ This function is used to return the ID given to it. find('key','entry')
        Key -> date, cust_email, cust_location, product_id, product_quantity
        Entry -> the value/s that you are looking for.
        """
        cur = self.cur
        con = self.database
        if key == "date":
            query = cur.execute("SELECT date, cust_email, cust_location, product_id, product_quantity FROM customer_orders WHERE date=?", [entry])
        elif key == "cust_email":
            query = cur.execute("SELECT date, cust_email, cust_location, product_id, product_quantity FROM customer_orders WHERE cust_email=?", [entry])
        elif key == "cust_location":
            query = cur.execute("SELECT date, cust_email, cust_location, product_id, product_quantity FROM customer_orders WHERE cust_location=?", [entry])
        elif key == "product_id":
            query = cur.execute("SELECT date, cust_email, cust_location, product_id, product_quantity FROM customer_orders WHERE product_id=?", [entry])
        elif key == "product_quantity":
            query = cur.execute("SELECT date, cust_email, cust_location, product_id, product_quantity FROM customer_orders WHERE product_quantity=?", [entry])
        else:
            print("Error: Key is out out of bounds.")
            pass
        
        repo = pd.DataFrame(cur.fetchall(), columns=['date', 'cust_email', 'cust_location', 'product_id', 'product_quantity'])
        print(repo)
        
    def add(self, entry):
        """ CRUD function, that inserts a series of variables into a new entry in the DB. """
        
        query = ('insert into customer_orders (date, cust_email, cust_location, product_id, product_quantity)' 'VALUES (:date, :cust_email, :cust_location, :product_id, :product_quantity)')
        new_entry = user_addition

        try: 
            cur = self.cur
            con = self.database
            con.execute(query, new_entry)
            con.commit()
        
        except Error as e:
            print(e)
            
        finally:
            if con:
                con.close()

    def edit(self, entry):
        """ This function edits the ID that is recived."""
        query = 'UPDATE customer_orders set date=?, cust_email=?, cust_location=?, product_id=?, product_quantity=? where date=?, cust_email=?, cust_location=?, product_id=?, product_quantity=?'
        updated_entry= user_update
        
        try:
            cur = self.cur
            con = self.database
            con.execute(query, updated_entry)
            con.commit()
        
        except Error as e:
            print(e)

        finally:
            if con:
                con.close()

    def delete(self, entry):
        """ This function deletes the ID currently being recieved. """
        query = 'DELETE from customer_orders where date=?, cust_email=?, cust_location=?, product_id=?, product_quantity=?'
        del_selection = user_deletion

        try:
            cur = self.cur
            con = self.database
            con.execute(query, del_selection)
            con.commit()

        except Error as e:
            print(e)
        
        finally:
            if con:
                con.close()

    def exit(self):
        """ This function will close out of the DB. """

        self.database.close()
