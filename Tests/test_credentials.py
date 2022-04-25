import unittest
from credentials import Credentials


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.new_credentials = Credentials('facebook', 'ed@gmail.com', 'ed', 'edd12345')

    def tearDown(self) -> None:
        Credentials.credential_list = []


if __name__ == '__main__':
    unittest.main()
