class User:
    '''
    Class that generates new instances of User
    '''

    user_list = []

    def __init__(self,first_name,last_name,user_name,email):
        '''
            __init__ method that helps us define properties for our objects.

            Args:
                first_name: New user first name.
                last_name : New user last name.
                user_name: New user user_name.
                email : New user email address.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user_name.

        Args:
            user_name: user_name to search for
        Returns :
            credentials of person that matches the user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user


class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    credentials_list=[]

    def __init__(self,user_name,password):

        """

        Args:
            user_name : New  credentials user name.
            password : New credentials password.

        self.user_name = user_name
        self.password = password


        """
        self.user_name = user_name
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

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user-name.

        Args:
            number: Phone number to search for
        Returns :
            credentials of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
                return credentials
