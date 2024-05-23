from flask import Blueprint, request, jsonify
from app.services.authentication_service import register_user, login_user
from app.middleware.jwt_middleware import token_required

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        print("Received data:", data)
        message, success = register_user(data['username'], data['email'], data['password'])
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400
    except Exception as e:
        print("Error in register:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500

@auth_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        token, success = login_user(data['email'], data['password'])
        if success:
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': token}), 401
    except Exception as e:
        print("Error in login:", str(e))
        return jsonify({'message': 'Internal Server Error'}), 500

@auth_blueprint.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'This is a protected route.', 'user_id': request.user_id}), 200