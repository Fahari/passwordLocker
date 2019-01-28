import unittest # Importing the unittest module
from user import User
from user import Credentials# Importing the user class

class TestUser(unittest.TestCase):
    """
    Class that generates new instances of contacts.
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Kevin","Kironji","Fahari","me@xyz.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Kevin")
        self.assertEqual(self.new_user.last_name,"Kironji")
        self.assertEqual(self.new_user.user_name,"Fahari")
        self.assertEqual(self.new_user.email,"me@xyz.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    Class that generates new instances of credentials.
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Fahari","12345678") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,"Fahari")
        self.assertEqual(self.new_credentials.password,"12345678")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the contact object is saved into
         the credentials_list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()
