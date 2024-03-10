import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_username(self):
        if not 6 <= len(self.username) <= 30:
            return False

        if not re.match(r'^[a-zA-Z0-9.]+$', self.username):
            return False

        if '..' in self.username:
            return False

        if re.search(r'[&=+<>,\'"\\|]', self.username):
            return False

        return True

    def check_password(self):
        if len(self.password) < 8 or len(self.password) > 128:
            return False

        if not any(c.isupper() for c in self.password) or not any(c.islower() for c in self.password):
            return False

        if not re.match(r'^[a-zA-Z0-9]+$', self.password):
            return False

        if not any(c.isdigit() for c in self.password):
            return False

        if not re.search(r'[~!@#$%^&*()_\-+[\]{}<>/?\\|\'".,:;]', self.password):
            return False

        return True

user1 = User("user123", "P@ssw0rd")
print("Username valid:", user1.check_username())
print("Password valid:", user1.check_password())

user2 = User("user..name", "weakpwd")
print("Username valid:", user2.check_username())
print("Password valid:", user2.check_password())
