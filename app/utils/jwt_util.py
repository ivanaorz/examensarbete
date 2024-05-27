import jwt
from datetime import datetime, timedelta, timezone
from config.default import SECRET_KEY  

def generate_token(user_id, author_name):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=1),  # Token expires in 1 day
        'iat': datetime.now(timezone.utc),
        'sub': user_id,
        'author_name': author_name
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload  # Returning the entire payload
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


