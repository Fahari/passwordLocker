class User:
    '''
    Class that generates new instances of User
    '''

    user_list = []

    def __init__(self,first_name,last_name,user_name,email):
            '''
                __init__ method that helps us define properties for our objects.

                Args:
                    first_name: New contact first name.
                    last_name : New contact last name.
                    user_name: New contact phone number.
                    email : New contact email address.
            '''

            self.first_name = first_name
            self.last_name = last_name
            self.user_name = user_name
            self.email = email
