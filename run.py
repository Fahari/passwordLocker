#!/usr/bin/env python3.6
from user import user
from user import Credentials

def create_user(fname,lname,username,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(user_name):
    '''
    Function that finds a user by user_name and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_user(user_name):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(user_name)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()





def create_credentials(username,email):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(username,email)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def find_credentials(user_name):
    '''
    Function that finds a credential by user_name and returns the credential
    '''
    return Credentials.find_by_user_name(user_name)

def check_existing_credentials(user_name):
    '''
    Function that check if a credential exists with that user_name and return a Boolean
    '''
    return Credentials.credential_exist(user_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
