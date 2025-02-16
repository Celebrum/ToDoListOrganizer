import unittest
import jwt
from src.user_auth import UserAuth, User, SECRET_KEY

class TestUserAuth(unittest.TestCase):

    def setUp(self):
        self.user_auth = UserAuth()

    def test_register(self):
        user = self.user_auth.register("testuser", "testpassword")
        self.assertEqual(user["username"], "testuser")
        self.assertIn("testuser", self.user_auth.users)

    def test_register_existing_user(self):
        self.user_auth.register("testuser", "testpassword")
        with self.assertRaises(ValueError):
            self.user_auth.register("testuser", "testpassword")

    def test_login(self):
        self.user_auth.register("testuser", "testpassword")
        token = self.user_auth.login("testuser", "testpassword")
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded_token["username"], "testuser")

    def test_login_invalid_user(self):
        with self.assertRaises(ValueError):
            self.user_auth.login("invaliduser", "testpassword")

    def test_login_invalid_password(self):
        self.user_auth.register("testuser", "testpassword")
        with self.assertRaises(ValueError):
            self.user_auth.login("testuser", "wrongpassword")

    def test_store_user_information_securely(self):
        user = self.user_auth.register("secureuser", "securepassword")
        self.assertTrue(user["username"], "secureuser")
        self.assertTrue(self.user_auth.users["secureuser"].check_password("securepassword"))

    def test_authentication_using_jwt(self):
        self.user_auth.register("jwtuser", "jwtpassword")
        token = self.user_auth.login("jwtuser", "jwtpassword")
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded_token["username"], "jwtuser")

if __name__ == '__main__':
    unittest.main()
