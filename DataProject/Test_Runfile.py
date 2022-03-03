""" This is the file that will have any testing
and be able to run for debugging or just running
the Program. """
import Operations 
import unittest



db = Operations.Ops('inventory.db')
db.formatTable()
db.find('cust_email', 'spib@aol.com')
db.saveChanges()
db.exit()

#app = db.databaseWarehouse()
#app.run()

