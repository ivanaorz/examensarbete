
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['my_mongodb_database']
users_collection = db['users']

class User:
    def __init__(self, username, email, password=None, password_hash=None, role='writer', _id=None):
        self.username = username
        self.email = email
        self.password = password
        self.password_hash = password_hash
        self.role = role
        self._id = _id
        if password:
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({'email': email})

    @staticmethod
    def insert_user(user_data):
        return users_collection.insert_one(user_data)
