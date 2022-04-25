import unittest
from credentials import Credentials


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.new_credentials = Credentials('facebook', 'ed@gmail.com', 'ed', 'edd12345')

    def tearDown(self) -> None:
        Credentials.credentials_list = []

    def test_credendtial_created(self):
        self.assertEqual(self.new_credentials.website, 'facebook')
        self.assertEqual(self.new_credentials.email, 'ed@gmail.com')
        self.assertEqual(self.new_credentials.username, 'ed')
        self.assertEqual(self.new_credentials.password, 'edd12345')

    def test_add_credential(self):
        self.new_credentials.add_credential()

        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_delete_credential(self):
        self.new_credentials.add_credential()

        test_credential = Credentials('tiktok', 'test@gmail.com', 'tiktoker', 'tiktoker9876')
        test_credential.add_credential()

        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_search_credential(self):
        self.new_credentials.add_credential()

        test_search = self.search_credentials('facebook')

        self.assertEqual(test_search, self.new_credentials)


if __name__ == '__main__':
    unittest.main()
