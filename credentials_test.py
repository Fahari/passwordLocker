import unittest
from user import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class that generates new instances of credentials.
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Facebook","12345678") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.platform,"Facebook")
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

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our credential list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("TestUser","123456789") # new credential
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_user_name(self):
        '''
        test to check if we can find a user by user_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("TestUser","123456789") # new contact
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_user_name("TestUser")

        self.assertEqual(found_credentials.password,test_credentials.password)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("TestUser","123456789") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("TestUser")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()
