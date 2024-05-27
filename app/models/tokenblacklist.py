from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['my_mongodb_database']
blacklist_collection = db['blacklist']

class BlacklistToken:
    def __init__(self, token):
        self.token = token

    @staticmethod
    def add_token_to_blacklist(token):
        blacklist_collection.insert_one({'token': token})

    @staticmethod
    def is_token_blacklisted(token):
        return blacklist_collection.find_one({'token': token}) is not None
