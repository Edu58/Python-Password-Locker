import unittest
from credentials import Credentials


class MyTestCase(unittest.TestCase):
    """This class tests the credentials.py functions"""

    def setUp(self) -> None:
        """Creates a new test credential for every test case to use"""
        self.new_credentials = Credentials('facebook', 'ed@gmail.com', 'ed', 'edd12345')

    def tearDown(self) -> None:
        """Clears up the credentials_list after every test case"""
        Credentials.credentials_list = []

    def test_credential_created(self):
        """Tests if the credential object is created successfully"""
        self.assertEqual(self.new_credentials.website, 'facebook')
        self.assertEqual(self.new_credentials.email, 'ed@gmail.com')
        self.assertEqual(self.new_credentials.username, 'ed')
        self.assertEqual(self.new_credentials.password, 'edd12345')

    def test_add_credential(self):
        """Tests if the credential object is added to the credential successfully"""
        self.new_credentials.add_credential()

        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_credentials(self):
        """Tests if all the credentials are returned successfully"""
        self.new_credentials.add_credential()

        test_credential = Credentials('instagram', 'inst@gmail.com', 'vapor', 'insta4234')
        test_credential.add_credential()

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_delete_credential(self):
        """Tests if the credential belonging to the provided website is deleted successfully"""
        self.new_credentials.add_credential()

        test_credential = Credentials('tiktok', 'test@gmail.com', 'tiktoker', 'tiktoker9876')
        test_credential.add_credential()

        self.new_credentials.delete_credential('facebook')
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_search_credentials(self):
        """Tests if the credential for the searched website is returned successfully"""
        self.new_credentials.add_credential()

        test_search = Credentials.search_credentials('facebook')

        self.assertEqual(test_search, self.new_credentials)

    def test_search_credentials_not_found(self):
        """Tests if an error is returned if a credential belonging to the provided website is not found"""
        self.new_credentials.add_credential()

        test_search = Credentials.search_credentials('instagram')

        self.assertEqual(test_search, 'No such credentials. Try adding them first or check your spelling and try again.')


if __name__ == '__main__':
    unittest.main()
