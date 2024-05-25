from app.models.books import Book
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_book_entry(user_id, title, author_name, genre, year):
    try:
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        
        new_book = Book(user_id=user_id, title=title, author_name=author_name, genre=genre, year=year)
        Book.insert_book(new_book.to_dict())
        return True, 'Book entry created successfully'
    except ValueError as ve:
        logger.error(f"Validation error in create_book_entry: {ve}")
        return False, str(ve)
    except Exception as e:
        logger.error(f"Error in create_book_entry: {e}")
        return False, 'An error occurred creating the book entry'

def get_books_by_user(user_id):
    try:
        books = Book.find_by_user_id(user_id)
        return True, books
    except Exception as e:
        logger.error(f"Error in get_books_by_user: {e}")
        return False, 'An error occurred displaying book entries'
   