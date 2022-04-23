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
    self.new_user = User("Eucabeth","Saniamo","1234") # create user object

def tearDown(self):
    '''
    tearDown method that cleans up after each test case is run
    '''

    User.user_list = []


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"Eucabeth")
    self.assertEqual(self.new_user.last_name,"Saniamo")
    self.assertEqual(self.new_user.password,"1234")
   






