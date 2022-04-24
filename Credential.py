import Credential
class Credential:

    '''
    class that creates instaces of user accounts
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
   
  




    
    