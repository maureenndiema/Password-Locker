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

        




    
    