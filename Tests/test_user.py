import unittest
from user import User


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.new_user = User('edwin', 'eddy123')

    def tearDown(self) -> None:
        User.users_list = []

    def test_if_user_is_created_correctly(self):
        self.assertEqual(self.new_user.username, 'edwin')
        self.assertEqual(self.new_user.password, 'eddy123')

    def test_add_user(self):
        self.new_user.add_user()
        self.assertEqual(len(self.new_user.users_list), 1)

    def test_delete_user(self):
        self.new_user.add_user()

        test_user = User('ed', 'ed456')
        test_user.add_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users_list), 1)

    def test_successful_login(self):
        self.new_user.add_user()

        correct_login = User.login('edwin', 'eddy123')
        self.assertTrue(correct_login)

    def test_failed_login(self):
        self.new_user.add_user()

        wrong_login = User.login('edwin', 'eddy12')
        self.assertFalse(wrong_login)


if __name__ == '__main__':
    unittest.main()
