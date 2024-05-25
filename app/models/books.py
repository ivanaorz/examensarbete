from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['my_mongodb_database']
books_collection = db['books']

class Book:
    def __init__(self, user_id, title, author_name, genre, year, _id=None):
        self.user_id = user_id
        self.title = title
        self.author_name = author_name
        self.genre = genre
        self.year = year
        self._id = _id if _id else ObjectId()

    def to_dict(self):
        return {
            '_id': self._id,
            'user_id': self.user_id,
            'title': self.title,
            'author_name': self.author_name,
            'genre': self.genre,
            'year': self.year
        }

    @staticmethod
    def insert_book(book_data):
        return books_collection.insert_one(book_data)
    
    @staticmethod
    def find_by_user_id(user_id):
        return list(books_collection.find({'user_id': user_id}))