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
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Fahari","me@xyz.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


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

        self.assertEqual(self.new_credentials.user_name,"Fahari")
        self.assertEqual(self.new_credentials.password,"12345678")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the contact object is saved into
         the credentials_list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("TestUser","123456789")
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

if __name__ == '__main__':
    unittest.main()
