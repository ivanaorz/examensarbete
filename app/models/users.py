
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient('mongodb://localhost:27017/')
db = client['my_mongodb_database']
users_collection = db['users']

# Creating a unique index on the 'email' field
users_collection.create_index('email', unique=True)

class User:
    def __init__(self, username, email, password=None, password_hash=None, role='writer', _id=None, author_name=None):
        self.username = username
        self.email = email
        self.password = password
        self.password_hash = password_hash
        self.role = role
        self._id = _id if _id else ObjectId()
        self.author_name = author_name
        if password:
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            '_id': self._id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'role': self.role,
            'authorName': self.author_name
        }

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({'email': email})

    @staticmethod
    def insert_user(user_data):
        try:
            return users_collection.insert_one(user_data)
        except DuplicateKeyError:
            raise ValueError("A user with this email already exists.")



