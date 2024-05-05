from flask_login import UserMixin

# Mock database of users
users = {
    "user@example.com": {"password": "securepassword", "id": "1"}
}

class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email

    @staticmethod
    def get(user_id):
        for email, user in users.items():
            if user['id'] == user_id:
                return User(user_id, email)
        return None

    @staticmethod
    def authenticate(email, password):
        if email in users and users[email]['password'] == password:
            return User(users[email]['id'], email)
        return None
