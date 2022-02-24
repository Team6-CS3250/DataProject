""" This is the file that will have any testing
and be able to run for debugging or just running
the Program. """
import DatabaseWarehouse as db
import unittest


class TestClasses(unittest.TestCase):

    pass


app = db.databaseWarehouse()
app.run()

