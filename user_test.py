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

def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
     the user list
    '''
    self.new_user.save_user() # saving the new user
    self.assertEqual(len(User.user_list),1)

   
def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple user
    objects to our user_list
    '''
    self.new_user.save_user()
    test_contact = User("Test","user","password") # new contact
    test_contact.save_user()
    self.assertEqual(len(User.user_list),2)

def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our user list
    '''
    self.new_user.save_user()
    test_user = User("Test","user","password") # new user
    test_user.save_user()

    self.new_user.delete_user()# Deleting a user object
    self.assertEqual(len(User.user_list),1)

def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0710909747","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_number("0710909747")

        self.assertEqual(found_user.email,test_user.email)

if __name__ == '__main__':
  unittest.main()





   






