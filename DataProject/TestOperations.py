import unittest
from DataProject.Operations import Ops

   
"""
   *README*
   Testing should be done in seperate classes, this is just a start to get the ducks in a row
   
   Asserts planned to use for testing
       
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
class test_operations(unittest.TestCase):
   def test_init(self):
      self.assertIsInstance(Ops.__init__)
      """Not done here still figuring out the testing fields"""

class test_formatTable(unittest.TestCase): 
   def test_formatTable(self):
      self.assertRaises(Ops.formatTable())
      """Working on fields again"""

class test_viewTable(unittest.TestCase):
   def test_viewTable(self):
      self.assertTrue(Ops.viewTable())
      """Working on fields"""
      
class test_saveChanges(unittest.TestCase):
   def test_saveChanges(self):
      self.assertTrue(Ops.saveChanges())

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
    
   def test_delete(self):
      result = self.Ops.delete()
      self.assertTrue(result.ok)

if __name__ == "__main__":
    unittest.main()