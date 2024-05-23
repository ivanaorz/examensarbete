# import sys
# import os

# # Add the parent directory of the backend folder to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


# from flask import Flask
# from flask_pymongo import PyMongo
# from config.default import SECRET_KEY  # Importing the SECRET_KEY from configuration
# from app.controllers import authentication_controller


# app = Flask(__name__)
# app.config.from_object('config.default')
# app.config['SECRET_KEY'] = SECRET_KEY  # Setting the secret key explicitly
# mongo = PyMongo(app)


import sys
import os
 # Add the parent directory of the backend folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import Flask
from flask_pymongo import PyMongo
from config.default import SECRET_KEY

app = Flask(__name__)
app.config.from_object('config.default')
app.config['SECRET_KEY'] = SECRET_KEY  # Setting the secret key explicitly
mongo = PyMongo(app)

# Import and register Blueprints
from app.controllers.authentication_controller import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Add other blueprints here in the future if needed