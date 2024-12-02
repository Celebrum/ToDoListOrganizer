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
