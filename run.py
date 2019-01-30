#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(fname,lname,username,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,username,email)
    return new_user

def create_credentials(platform,password):

    new_credentials = Credentials(platform,password)
    return new_credentials

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credentials.generate_password()
	return gen_pass


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credentials(credentials):

    credentials.save_credentials()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credentials(credentials):

    credentials.delete_credentials()


def find_user(user_name):
    '''
    Function that finds a user by user_name and returns the user
    '''
    return User.find_by_user_name(user_name)

def find_credentials(user_name):

    return Credentials.find_by_email(user_name)


def check_existing_user(user_name):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(user_name)

def check_existing_credential(user_name):

    return Credential.credential_exist(user_name)


def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def display_credential():

    return Credential.display_credential()




# def create_credentials(username,email):
#     '''
#     Function to create a new credential
#     '''
#     new_credentials = Credentials(username,email)
#     return new_credentials
#
# def save_credentials(credentials):
#     '''
#     Function to save credentials
#     '''
#     credentials.save_credentials()
#
# def del_credentials(credentials):
#     '''
#     Function to delete a credential
#     '''
#     credentials.delete_credentials()
#
# def find_credentials(user_name):
#     '''
#     Function that finds a credential by user_name and returns the credential
#     '''
#     return Credentials.find_by_user_name(user_name)
#
# def check_existing_credentials(user_name):
#     '''
#     Function that check if a credential exists with that user_name and return a Boolean
#     '''
#     return Credentials.credential_exist(user_name)
#
# def display_credentials():
#     '''
#     Function that returns all the saved credentials
#     '''
#     return Credentials.display_credentials()




def main():
    print("Hello Welcome to passwordLocker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:


        # print("Use these short codes : cc - create new credentials, dc - display credentials, fc -find credentials, ex -exit passwordLocker")

        print("Use these short codes : ")
        print("cc - Create New Credentials")
        print("dc - Display Credentials")
        print("fc - Find Credentials")
        print("ca - Create a Social Account")
        print("da - Display Social Account")
        print("da - Delete Social Account")
        print("ex - Exit the list")


        short_code = input().lower()

        if short_code == 'cc':

            print("New Credentials")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Username ...")
            u_name = input()

            print("Email address ...")
            e_address = input()

            print("Password ...")
            e_pass = input()

            save_user(create_user(f_name,l_name,u_name,e_address)) # create and save new contact.
            print ('\n')
            print(f"New Credentials {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_user():
                    print("Here is a list of all your saved credentials")
                    print('\n')

                    for user in display_user():
                            print(f"{user.first_name} {user.last_name} .....{user.user_name}")

                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == 'fc':

                print("Enter the username you want to search for")

                search_number = input()

                if check_existing_user(search_number):
                        search_user = find_user(search_number)
                        print(f"{search_user.first_name} {search_user.last_name}")
                        print('-' * 20)

                        # print(f"Phone number.......{search_contact.phone_number}")
                        print(f"Email address.......{search_user.email}")
                else:
                        print("That credential does not exist")

        elif short_code == 'ca':

            print("Do you want password to auto-generate.. Use below options")
            print("Option 1: YY -- Yes")
            print("Option 2: NN -- No")
            print("Option 3: EX -- Exit the Social Accounts")

            pass_auto = input().lower()

            if pass_auto == 'yy':
                print("Password will be auto generated")
                print ("Enter Email Address .....")
                e_mail = input()

                print("Platform Account (Social Account)...")
                p_account = input()

                print("Enter Password ...")
                p_word = generate_password()

                save_credentials(create_credentials(e_mail,p_account))

                print ('\n')

                print(f" New Credentials for {e_mail} {p_account} created. Password is {p_word}")

                print ('\n')

            elif pass_auto =='nn':

                print ("Enter Email Address ....")
                e_mail = input()

                print("Platform Account (Social Account)...")
                p_account = input()

                print("Enter Password ...")
                p_word = input()

                save_credentials(create_credentials(e_mail,p_account,p_word))

                print ('\n')

                print(f" New Credential for {e_mail} {p_account} created. Password is {p_word}")

                print ('\n')

            elif pass_auto == "ex":

                print("Bye .......")


            else:
                print("Wrong option try again")

                print("Do you want password to auto-generate.. Use below options")
                print("Option 1: YY -- Yes")
                print("Option 2: NN -- No")
                print("Option 3: EX -- Exit the Social Accounts")

                pass_auto = input().lower()

        elif short_code == 'da':

            if display_credentials():
                print("Here is a list of all your credential")

                print('\n')

                for credentials in display_credentials():

                        print(f"{credentials.email} {credentials.platform} .....{credentials.password}")
                        print('\n')

            else:

                print('\n')

                print("You don't seem to have any credentials saved yet")

                print('\n')

        elif short_code == "de":

            print("Starting to delete .......")
            print("Enter Email .......")
            del_name = input(" ")

            delete_credentials(del_name)

        elif short_code == "ex":

            print("Bye .......")

            break

        else:

            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
