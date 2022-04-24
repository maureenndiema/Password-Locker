import unittest
from Credential import Credential
import pyperclip

class TestCredential(unittest.TestCase):
    
    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_credential = Credential("GitHub", "ndiemam@gmail.com", "maureenndiema")
    
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_credential.account, "GitHub")
        self.assertEqual(self.new_credential.email, "ndiemam@gmail.com")
        self.assertEqual(self.new_credential.passlock, "maureenndiema")

    def test_save_credential(self):
        '''
        check if credential can be saved
        '''  
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


    







if __name__ == '__main__':
  unittest.main()
