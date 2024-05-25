from flask import Blueprint, request, jsonify
from app.services.book_service import create_book_entry, get_books_by_user
from app.middleware.jwt_middleware import token_required

book_blueprint = Blueprint('books', __name__)
   
@book_blueprint.route('/create', methods=['POST']) #CREATE
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
    
@book_blueprint.route('/all', methods=['GET'])  # READ
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
