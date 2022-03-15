"""*README*
    Testing should be done in seperate classes, this is just a start to get the ducks in a row
"""

"""Asserts planned to use for testing
    -assertRaises and assertEquals could be good too for DatabaseWarehouse _init_
    -assertEquals for DatabaseWarehouse item_selected (testing line that it moves to)
    -assertIsInstance for DatabaseWarehouse run
    -assertIsInstance for Operations _init_
    -assertIsInstance for Operations viewTable maybe assertTrue
    -assertIsInstance for Operations saveChanges maybe assertTrue
    -assertIsInstance for Operations view maybe assertTrue
    -assertEquals for Operations find (believe this should find the line that the info is on and should equal line)
    -assertTrue for Operations add, edit, delete, & exit
    -assertRaises? for CRUD_Operations create (Maybe IsInstance, need more info)
    -assertTrue for CRUD_Operations read
    -assertTrue for CRUD_Operations update
    -assertTrue for CURD_Operations delete
"""

import unittest

# class test_operations(unittest.TestCase):

   # def test_init(self):
        
#class test_format_table(unittest.TestCase):
#class test_view_table(unittest.TestCase):
#class test_save_changes(unittest.TestCase):
#class test_view(unittest.TestCase):
#class test_find(unittest.TestCase):

class test_add(unittest.TestCase):
    def teardown(self):
        self.Ops.delete()
    
    def setUp(self):
        self.Ops.formatTable()
    
    def test_add(self):
        result = self.Ops.add()
        self.assertTrue(result.ok)

class test_edit(unittest.TestCase):
    def teardown(self):
        self.Ops.delete()
    
    def setUp(self):
        self.Ops.formatTable()
    
    def test_edit(self):
        result = self.Ops.edit()
        self.assertTrue(result.ok)

class test_delete(unittest.TestCase):
    def teardown(self):
        self.Ops.delete()
    
    def setUp(self):
        self.Ops.formatTable()
    
    def test_add(self):
        result = self.Ops.delete()
        self.assertTrue(result.ok)