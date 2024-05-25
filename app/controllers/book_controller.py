from flask import Blueprint, request, jsonify
from app.services.book_service import create_book_entry, get_books_by_user, update_book_entry, delete_book_entry, get_authors_with_books, get_books_by_author_name
from app.middleware.jwt_middleware import token_required

book_blueprint = Blueprint('books', __name__)
   
@book_blueprint.route('/create', methods=['POST']) #CREATE BOOK ENTRY
@token_required
def create_book():
    try:
        data = request.json
        if not data or not all(key in data for key in ('title', 'author_name', 'genre', 'year')):
            return jsonify({'message': 'All fields are required'}), 400
        
        # Ensuring the author_name from token matches the one in request
        if data['author_name'] != request.user_author_name:
            return jsonify({'message': 'Author name from token does not match the one in request'}), 403

        title = data['title']
        author_name = data['author_name']
        genre = data['genre']
        year = data['year']

        if not isinstance(year, int):
            return jsonify({'message': 'Year must be an integer'}), 400

        print(f"Creating book with title: {title}, author_name: {author_name}, genre: {genre}, year: {year}")

        success, message = create_book_entry(request.user_id, title, author_name, genre, year)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400
    except Exception as e:
        print("Error in create_book:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500
    
@book_blueprint.route('/all', methods=['GET'])  # READ ALL BOOK ENTRIES
@token_required
def get_books():
    try:
        success, result = get_books_by_user(request.user_id)
        if success:
            if not result:
                return jsonify({'message': 'There are no book entries yet.'}), 200
            return jsonify({'books': result}), 200
        else:
            return jsonify({'message': result}), 500
    except Exception as e:
        print("Error in get_books:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500    
    
@book_blueprint.route('/update', methods=['PUT'])  # UPDATE BOOK ENTRY
@token_required
def update_book():
    try:
        data = request.json
        if not data or not all(key in data for key in ('title', 'new_title', 'new_author_name', 'new_genre', 'new_year')):
            return jsonify({'message': 'All fields are required'}), 400

        if data['new_author_name'] != request.user_author_name:
            return jsonify({'message': 'Author name from token does not match the new author name in request'}), 403

        user_id = request.user_id
        title = data['title']
        new_title = data['new_title']
        new_author_name = data['new_author_name']
        new_genre = data['new_genre']
        new_year = data['new_year']

        if not isinstance(new_year, int):
            return jsonify({'message': 'Year must be an integer'}), 400

        success, message = update_book_entry(user_id, title, new_title, new_author_name, new_genre, new_year)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400
    except Exception as e:
        print("Error in update_book:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500    
    
@book_blueprint.route('/delete', methods=['DELETE'])  # DELETE BOOK ENTRY
@token_required
def delete_book():
    try:
        data = request.json
        if not data or not 'title' in data:
            return jsonify({'message': 'Title is required'}), 400

        user_id = request.user_id
        title = data['title']

        success, message = delete_book_entry(user_id, title)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400
    except Exception as e:
        print("Error in delete_book:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500  

@book_blueprint.route('/authors', methods=['GET'])  #READ ALL AUTHORS WITH BOOKS
def get_authors():
    try:
        success, authors = get_authors_with_books()
        if success:
            return jsonify({'authors': sorted(authors)}), 200
        else:
            return jsonify({'message': 'An error occurred while retrieving the list with self-published writers.'}), 500
    except Exception as e:
        print("Error in get_authors:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500    

@book_blueprint.route('/author/<author_name>', methods=['GET'])  #READ ALL BOOKS OF A PARTICULAR AUTHOR
def get_books_by_author(author_name):
    try:
        success, books = get_books_by_author_name(author_name)
        if success:
            if not books:
                return jsonify({'message': f'No books found for author: {author_name}'}), 200
            return jsonify({'books': books}), 200
        else:
            return jsonify({'message': 'An error occurred while retrieving books for the author.'}), 500
    except Exception as e:
        print("Error in get_books_by_author:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500     
