from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['my_mongodb_database']

class User:
    def __init__(self, username, email, password, role='writer'):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role
    
    @staticmethod
    def find_by_email(email):
        return db.users.find_one({'email': email})
    
    @staticmethod
    def insert_user(user_data):
        return db.users.insert_one(user_data)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)