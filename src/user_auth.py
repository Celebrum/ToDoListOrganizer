import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = 'your_secret_key'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("User already exists")
        user = User(username, password)
        self.users[username] = user
        self.validate_user_data(user)
        return {"username": username}

    def login(self, username, password):
        user = self.users.get(username)
        if not user or not user.check_password(password):
            raise ValueError("Invalid username or password")
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        return token

    def ensure_ffed_compatibility(self):
        # Placeholder for ensuring compatibility with FfeD framework
        pass

    def validate_user_data(self, user):
        # Input validation
        if not user.username or not user.password:
            raise ValueError("User data is incomplete")
        # Data cleaning
        user.username = user.username.strip()
        user.password = user.password.strip()

    def validate_all_users(self):
        for user in self.users.values():
            self.validate_user_data(user)
