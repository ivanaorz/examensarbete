from app.models.users import User
from app.utils.jwt_util import generate_token

def register_user(username, email, password):
    try:
        existing_user = User.find_by_email(email)
        if existing_user:
            return 'User already exists', False
        new_user = User(username, email, password)
        User.insert_user(new_user.__dict__)
        return 'User registered successfully', True
    except Exception as e:
            print("Error in register_user:", str(e))
            return 'Internal Server Error', False

def login_user(email, password):
    try:
        user_data = User.find_by_email(email)
        if user_data and User(**user_data).check_password(password):
            token = generate_token(user_data['_id'])
            return token, True
        return 'Invalid credentials', False
    except Exception as e:
        print("Error in login_user:", str(e))
        return 'Internal Server Error', False