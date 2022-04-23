class User:
    """
    class that generates new instance of user
    """

    user_list = []

    def _init_(self, user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user(self):

        """
        save_user method saves a new user objects to the user_list
        """

        User.save_user.append(self)

   
    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)

    
    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user

    

        

        
        
