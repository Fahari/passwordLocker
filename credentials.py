import pyperclip
import string
import random

class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    credentials_list=[]

    def __init__(self,platform,password):

        """

        Args:
            user_name : New  credentials user name.
            password : New credentials password.

        self.user_name = user_name
        self.password = password


        """
        self.platform = platform
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):

        gen_pass=''.join(random.choice(char) for _ in range(size))

        return gen_pass

    @classmethod
    def credentials_exist(cls,user_name):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            user_name: user_name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
