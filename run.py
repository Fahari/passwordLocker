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

def del_contact(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
