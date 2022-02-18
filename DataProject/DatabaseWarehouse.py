import Operations
import PyQt5.QtWidgets
import sys

class databaseWarehouse(Operations):
    """
    This class will be the backend for the GUI, Creating
    the Interface for the Database. Using the methods from
    Operations to use the Database.
    There should be buttons/dropdowns for the following functions:
    - Call (Locate one or multiple IDs, and Search critera.)
    - Add (Ask if you want to save before doing another command)
    - Edit (Ask if you want to save before doing another command)
    - Delete (Ask for comformation)
    - Browse (Shows all IDs in DB)
    - Save Changes (Just commits any changes)
    - Save Copy (Saves any number of selected IDs to another file)
    - Exit (Ask if you want to save if any changes were made)
    """

    def __init__(self):
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        window = PyQt5.QtWidgets.QWidget()

        pass
