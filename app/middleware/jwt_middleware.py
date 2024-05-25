from flask import request, jsonify
from functools import wraps
from app.utils.jwt_util import decode_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
            else:
                return jsonify({'message': 'Invalid authorization header'}), 403
        else:
            return jsonify({'message': 'Authorization header is missing'}), 403

        decoded_token = decode_token(token)
        if isinstance(decoded_token, str):
            return jsonify({'message': decoded_token}), 403
        
        request.user_id = decoded_token['sub']
        request.user_author_name = decoded_token.get('author_name', '')

        return f(*args, **kwargs)
    return decorated
