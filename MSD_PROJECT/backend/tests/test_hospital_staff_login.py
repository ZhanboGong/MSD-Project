import unittest
from hospital_staff_login import login, users

class TestHospitalStaffLogin(unittest.TestCase):

    def test_valid_login(self):
        # 测试有效的用户名和密码
        for username, password in users.items():
            with self.subTest(username=username, password=password):
                login(username, password)
                self.assertIn('Welcome', str(login.output))

    def test_invalid_username(self):
        # 测试无效的用户名
        invalid_usernames = ["nonexistent_user", "staff1@example.com", "doctor1"]
        valid_password = list(users.values())[0]
        for username in invalid_usernames:
            with self.subTest(username=username, password=valid_password):
                login(username, valid_password)
                self.assertIn('Invalid', str(login.output))

    def test_invalid_password(self):
        # 测试无效的密码
        invalid_passwords = ["wrongpassword", "invalid", ""]
        valid_username = list(users.keys())[0]
        for password in invalid_passwords:
            with self.subTest(username=valid_username, password=password):
                login(valid_username, password)
                self.assertIn('Invalid', str(login.output))

if __name__ == '__main__':
    unittest.main()