import pyperclip
import Credential
class Credential:

    '''
    class that creates instances of user accounts
    '''
   
    credential_list = []
    
    '''
    init method to define properties of our objects
    ''' 
  
    def __init__(self, account , email , passlock):

        self.account = account
        self.email = email
        self.passlock = passlock

   
    def save_credential(self):
        '''
        self credentials in credential_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete credential 
        '''
        Credential.credential_list.remove(self) 


    @classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return credential 

    
    @classmethod
    def credential_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False  

    @classmethod
    def display_credential(cls):
        '''
        method that returns all credential
        '''
        return cls.credential_list


    @classmethod
    def passlock(cls, account):
            find_account = Credential.find_account(account)
            pyperclip.copy(find_account.passlock)    
             
   
  




    
    