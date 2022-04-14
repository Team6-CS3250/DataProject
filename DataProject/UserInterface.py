
class UserInterface():
    """ The user intercace class will store the objects input by the user
        to be used in the operations class."""

        
    # Name of the .csv to be loaded into the databse
    file_name = None

    # The key chosen and then input by user that will be used to search the database 
    # (do I need to make this specfic to the type?)
    search_key = None

    # New (single) entry input by user to be loaded into the database
    user_addition = None

    # Revised entry that has been updated by user to be updated in database
    user_update = None

    # Entry chosen by user to be deleted from database 
    # (will input be a click or a string entry?)
    user_deletion = None

