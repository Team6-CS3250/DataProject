import unittest
from DataProject.Operations import Ops
import Operations

class TestOperations(unittest.TestCase):        
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
        """"
      def test_init(self):
        self.assertIsInstance(Ops.__init__)"""Not done here still figuring out the testing fields"""

      def test_formatTable(self):
         self.assertRaises(Ops.formatTable())
         """Working on fields again"""
      
      def test_viewTable(self):
         self.assertTrue(Ops.viewTable())
         """Working on fields"""
      
      def test_saveChanges(self):
         self.assertTrue(Ops.saveChanges())
      