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


if __name__ == '__main__':
    unittest.main()
