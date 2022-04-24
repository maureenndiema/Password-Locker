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

