from Credential import Credential
from user import User
import random


def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

def save_credential(credential):

    '''
    method save credential  account
    '''

    credential.save_credential

def find_user(username):
    '''
    method for find user using username
    '''
    return User.find_user(username)

def create_credential(account, email, passlock):
    '''
    method credential details
    '''
    new_credential = Credential(account, email, passlock)
    return new_credential

    

