import unittest

from user import login
from user import check_password


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        self.username = 'test'
        self.success_password = '123123abc'

    def test_login_successfully(self):
        self.assertEqual("Hello, test", login(self.username, self.success_password))
        self.username = 'not_test_user'

    def test_login_invalid(self):
        self.assertEqual("Invalid credentials for user test", login(
            self.username, "test password"
        ))

    def test_check_password_correct(self):
        self.assertTrue(check_password("123123abc"))

    def test_check_password_wrong(self):
        self.assertFalse(check_password("random pwd"))


# if __name__ == '__main__':
#     unittest.main()
