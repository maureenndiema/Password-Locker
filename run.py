import random
from User import User
from Credential import Credential

def create_user(user_name, password):

 '''
 Function to create a new account
 '''

 new_user = User(user_name, password)
 return new_user

 
