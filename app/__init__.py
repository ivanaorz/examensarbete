import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from config.default import SECRET_KEY


app = Flask(__name__)
CORS(app)
app.config.from_object('config.default')
app.config['SECRET_KEY'] = SECRET_KEY 
mongo = PyMongo(app)


from app.controllers.authentication_controller import auth_blueprint
from app.controllers.book_controller import book_blueprint  
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(book_blueprint, url_prefix='/books')




