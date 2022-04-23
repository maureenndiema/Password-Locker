class User:
    '''
    class that generates new instance of user
    '''

    user_list = []

    def _init_(self, user_name,password):
        self.user_name = user_name
        self.password = password
        
