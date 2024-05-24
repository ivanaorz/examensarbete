from app.models.users import User
from app.utils.jwt_util import generate_token
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def register_user(username, email, password, author_name):
    try:
        existing_user = User.find_by_email(email)
        if existing_user:
            return 'User already exists', False
        new_user = User(username=username, email=email, password=password, author_name=author_name)
        # new_user = User(username, email, password, author_name)
        User.insert_user(new_user.__dict__)
        return 'User registered successfully', True
    except Exception as e:
            print("Error in register_user:", str(e))
            return 'Internal Server Error', False


    
def login_user(email, password):
    try:
        user_data = User.find_by_email(email)
        if user_data:
            user = User(
                username=user_data.get('username'),
                email=user_data.get('email'),
                password_hash=user_data.get('password_hash'),  
                role=user_data.get('role'),
                _id=user_data.get('_id')
            )
            if user.check_password(password):
                token = generate_token(str(user._id))
                return token, True
        return 'Invalid credentials', False
    except Exception as e:
        logger.error(f"Error in login_user: {e}")
        return 'Internal Server Error', False    
