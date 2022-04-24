from click import password_option
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

def save_credential(credential):
    '''
    save credentials
    '''
    credential.save_credential()

def display_credential():
    '''
    method to display all the saved credential
    '''
    return Credential.display_credential()

def find_account(account):
    '''
    method to search for an account
    '''
    return Credential.find_account(account)

def delete_credential(account):
    '''
    method to delete account
    '''
    account.delete_credential()

def main():
    # Dealing user class first
    print("Welcome to Password Locker! Please enter your name:  ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print('\n')
    print("*" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("*" * 80)

    while True:
        short_code = input().lower()

        if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            save_user(create_useraccount(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)

            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80)

        elif short_code == "ca":
            print("Enter account details: ")
            print("Account Name(e.g:Twitter): ")
            account = input()
            print("Email: ")
            email = input()

            print("Would you like a generated password?")
            if input()=="yes":
                letters= "ghijklmnopqrstuvwxyz0123456789FGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                passlock = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(passlock)
                save_credential(create_credential(account, email, passlock))
                print("Credential saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)

            elif input() == "no":
                print("Password: ")
                passlock=input()
                save_credential(create_credential(account, email, passlock))
                print("Credential saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)

                save_user(create_credential(account, email,passlock)) # create and save new passlock.
                save_credential(create_credential(account, email,passlock))
                print ('\n')
                print(f"New User {account} {email} created")
                print ('\n')

            else:
                print("i dont get it please use shortcode 'ca' and start again")

        elif short_code == "da":
            print(f"These are your credentials for {name}:")
            print("*" * 30)
            for Credential in display_credential():
                print(f"{Credential.account}\n {Credential.email}\n {Credential.passlock}")
            else:
                print("*" * 30)
                print("If empty, you do not have any accounts saved")

        elif short_code == "fa":
            print("Key in  the account you are searching for (ie.'Facebook'): " )
            search_credential= input()
            if find_account(search_credential):
                search_acc = find_account(search_credential)
                print(f"{search_acc.account} {search_acc.email} { search_acc.passlock}")
            else: print("This account does not exist")

        elif short_code == "gp":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)

        elif short_code == 'ex':
            print("*"*30)
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
            print("*"*30)
            break

        else:
            print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")

if __name__ == '__main__':
    main()  








