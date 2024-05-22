from flask import Flask, request, jsonify
from services.authentication_service import register_user, login_user

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

if __name__ == '__main__':
    app.run(debug=True)

    