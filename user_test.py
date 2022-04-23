import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
     '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
   
    # First Test
def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = User("Maureen","Ndiema","0710909747","ndiemam@gmail.com") # create user object




