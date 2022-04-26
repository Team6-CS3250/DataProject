from sqlite3 import *
import pandas as pd
import os


class Ops():
    """ 
    The Operations File containes all of the operator classes to interact with
    the data in the Database, with callable functions for the Gui to use.
    """
    

    def __init__(self, db_file):
        """ On call from GUI, this initaits by connecting to the DB. """

        # In addition to accessing the customer_orders.db, is it not important to 
        # also include the inventory.db in all these operations
        
        #db_file = UserInterface.file_name
        con = None
        self.table = 'customer_orders'
        try: #Trying to connect to the given DB file path.
            self.database = connect(db_file)
            print(version)
            self.cur = self.database.cursor()

        except Error as e: #Returns the error type, if the DB was unable to be connected to.
            print(e)

        finally: #Closes the DB if an Error occures.
            if con:
                con.close()

    def TableSwitch(self):
        """Switch table to product table instead of orders table."""

        if self.table == 'customer_orders':
            self.table = 'inventory_items'
        else:
            self.table = 'customer_orders'

            

    def formatTable(self):
        """Fixer method that is to format the table, use only if the table is not in the DB. """
        
        target_path_1 = os.path.join(os.path.dirname(__file__), 'customer_orders_team6.csv')
        print(target_path_1)
        target_path_2 = os.path.join(os.path.dirname(__file__), 'inventory_team6.csv')
        print(target_path_2)

        data = pd.read_csv(target_path_1)
        cur = self.database.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS customer_orders(date TEXT, cust_email TEXT, cust_location INTEGER, product_id TEXT, product_quantity INTEGER, trade_number INTEGER)")
        data.to_sql('customer_orders', self.database, if_exists='replace', index=False)
        self.database.commit()

        data = pd.read_csv(target_path_2)
        cur = self.database.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS inventory(product_id TEXT, quantity INTEGER, wholesale_cost REAL, sale_price REAL, supplier_id TEXT, entry_number INTEGER)")
        data.to_sql('inventory', self.database, if_exists='replace', index=False)
        self.database.commit()



    def viewTable(self):
        """ Converts DB to readable table then returns it. """
        if self.table = 'customer_orders':
            cur = self.database.cursor()
            con = self.database        
            cur.execute("SELECT * FROM customer_orders")
            df = pd.read_sql_query("SELECT * from customer_orders", con)
            return(df)

        elif self.table = 'inventory':
            cur = self.database.cursor()
            con = self.database        
            cur.execute("SELECT * FROM inventory")
            df = pd.read_sql_query("SELECT * from inventory", con)
            return(df)

    def saveChanges(self):
        """ When called it saves any changes that were made to the DB."""

        self.database.commit()

    def find(self, date, email, loc, prod, qt):
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
        
        repo = pd.DataFrame(cur.fetchall(), columns=['date', 'cust_email', 'cust_location', 'product_id', 'product_quantity', 'trade_number'])
        print(repo)
        
    def add(self, new_entry):
        """ CRUD function, that inserts a series of variables into a new entry in the DB. """
        if self.table == 'cutomer_orders':
            query = 'INSERT INTO customer_orders(date, cust_email, cust_location, product_id, product_quantity, trade_number) VALUES(?, ?, ?, ?, ?, ? + 1)'
            try: 
                cur = self.cur
                con = self.database
                cur.execute('SELECT MAX(trade_number) FROM customer_orders')
                val = cur.fetchone()
                list(val)
                for i in range(len(new_entry)):
                    if new_entry[i] == new_entry[5]:
                        new_entry[i] = val[0]
                cur.execute(query, new_entry)
                con.commit()
        
            except Error as e:
                print(e)
            
            finally:
                if con:
                    con.close()

        elif self.table == 'inventory':
            query = 'INSERT INTO inventory(product_id, quantity, wholesale_cost, sale_price, supplier_id, entry_number) VALUES(?, ?, ?, ?, ?, ? + 1)'
            try: 
                cur = self.cur
                con = self.database
                cur.execute('SELECT MAX(entry_number) FROM inventory')
                val = cur.fetchone()
                list(val)
                for i in range(len(new_entry)):
                    if new_entry[i] == new_entry[5]:
                        new_entry[i] = val[0]
                cur.execute(query, new_entry)
                con.commit()
        
            except Error as e:
                print(e)
            
            finally:
                if con:
                    con.close()

    def edit(self, entry):
        """ This function edits the ID that is recived."""
        if self.table == 'customer_orders':
            query = "UPDATE customer_orders SET date = ?, cust_email = ?, cust_location = ?, product_id = ?, product_quantity = ? WHERE trade_number = ?"       
            try:
                cur = self.cur
                con = self.database
                cur.execute(query, entry)
                con.commit()
        
            except Error as e:
                print(e)

            finally:
                if con:
                    con.close()

        elif self.table == 'inventory':
            query = "UPDATE inventory SET product_id = ?, quantity = ? , wholesale_cost = ?, sale_price = ?, supplier_id = ? WHERE entry_number = ?"       
            try:
                cur = self.cur
                con = self.database
                cur.execute(query, entry)
                con.commit()
        
            except Error as e:
                print(e)

            finally:
                if con:
                    con.close()

    def delete(self, entry):
        """ This function deletes the ID currently being recieved. """
        num = entry[5]
        query = ('DELETE FROM customer_orders WHERE trade_number = ' + num )
        print(query)
        try:
            cur = self.cur
            con = self.database
            cur.execute(query)
            con.commit()

        except Error as e:
            print(e)
        
        finally:
            if con:
                con.close()

    def exit(self):
        """ This function will close out of the DB. """
        
        self.database.close()