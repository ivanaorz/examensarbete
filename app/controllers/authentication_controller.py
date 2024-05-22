from flask import Flask, request, jsonify
from app.services.authentication_service import register_user, login_user
from app.middleware.jwt_middleware import token_required

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    message, success = register_user(data['username'], data['email'], data['password'])
    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'message': message}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    token, success = login_user(data['email'], data['password'])
    if success:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': token}), 401

@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'This is a protected route.', 'user_id': request.user_id}), 200    

# if __name__ == '__main__':
#     app.run(debug=True)

    