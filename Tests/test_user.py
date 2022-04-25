import unittest
from user import User


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.new_user = User('edwin', 'eddy123')

    def tearDown(self) -> None:
        self.new_user.users_list = []

    def test_if_user_is_created_correctly(self):
        self.assertEqual(self.new_user.username, 'edwin')
        self.assertEqual(self.new_user.password, 'eddy123')

    def test_add_user(self):
        self.new_user.add_user()
        self.assertEqual(len(self.new_user.users_list), 1)


if __name__ == '__main__':
    unittest.main()
