import unittest
from DataProject.DatabaseWarehouse import databaseWarehouse
import DatabaseWarehouse

Class TestDatabaseWarehouse(unittest.TestCase):

        """
        -assertRaises and assertEquals could be good too for DatabaseWarehouse _init_
        -assertEquals for DatabaseWarehouse item_selected (testing line that it moves to)
        -assertIsInstance for DatabaseWarehouse run
        -assertIsInstance for Operations _init_
        """
        """Have no clue what to do for __init__ method"""
    def test_run(self):
        self.assertIsInstance(databaseWarehouse.run(self), self)

    def test_itemSelected(self):
        self.assertEquals(databaseWarehouse.item_selected(event), self)

