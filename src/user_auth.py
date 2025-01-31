import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def check_password(self, password):
        return self._password == password

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = User(username, password)
        return {"username": username}

    def login(self, username, password):
        if username not in self.users:
            raise ValueError("Invalid username")
        user = self.users[username]
        if not user.check_password(password):
            raise ValueError("Invalid password")
        token = jwt.encode({"username": username}, SECRET_KEY, algorithm='HS256')
        return token
