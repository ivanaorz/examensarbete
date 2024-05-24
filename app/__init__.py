import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import Flask
from flask_pymongo import PyMongo
from config.default import SECRET_KEY


app = Flask(__name__)
app.config.from_object('config.default')
app.config['SECRET_KEY'] = SECRET_KEY 
mongo = PyMongo(app)


from app.controllers.authentication_controller import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
