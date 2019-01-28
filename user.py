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
                user_name: New user phone number.
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


class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    credentials_list=[]

    def __init__(self,account_name,password):

        """

        Args:
            account_name : New  credentials account name.
            password : New credentials password.

        self.account_name = account_name
        self.password = password


        """
        self.account_name = account_name
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
