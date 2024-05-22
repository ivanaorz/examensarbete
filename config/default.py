import os

MONGO_URI = 'mongodb://localhost:27017/my_mongodb_database'

SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')