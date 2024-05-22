from flask import request, jsonify
from functools import wraps
from app.utils.jwt_util import decode_token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        user_id = decode_token(token)
        if isinstance(user_id, str):
            return jsonify({'message': user_id}), 403
        
        request.user_id = user_id
        return f(*args, **kwargs)
    return decorated

