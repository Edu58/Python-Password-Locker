import unittest
from user import User


class MyTestCase(unittest.TestCase):

    """Creates a new test user for every test case to use"""
    def setUp(self):
        self.new_user = User('edwin', 'eddy123')

    """Clears up the user_list after every test case"""
    def tearDown(self) -> None:
        User.users_list = []

    """Tests if the user object is created successfully"""
    def test_if_user_is_created_correctly(self):
        self.assertEqual(self.new_user.username, 'edwin')
        self.assertEqual(self.new_user.password, 'eddy123')

    """Tests if the created user is successfully added to the user_list"""
    def test_add_user(self):
        self.new_user.add_user()
        self.assertEqual(len(self.new_user.users_list), 1)

    """Tests if the a user is successfully deleted from the user_list"""
    def test_delete_user(self):
        self.new_user.add_user()

        test_user = User('ed', 'ed456')
        test_user.add_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.users_list), 1)

    """Tests if the user is logged in successfully on entering correct details"""
    def test_successful_login(self):
        self.new_user.add_user()

        correct_login = User.login('edwin', 'eddy123')
        self.assertTrue(correct_login)

    """Tests if the user is blocked from logging in if the details provided are wrong"""
    def test_failed_login(self):
        self.new_user.add_user()

        wrong_login = User.login('edwin', 'eddy12')
        self.assertFalse(wrong_login)


if __name__ == '__main__':
    unittest.main()
