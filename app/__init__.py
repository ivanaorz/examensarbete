from flask import Flask
from flask_pymongo import PyMongo
from config.default import SECRET_KEY  # Importing the SECRET_KEY from configuration

app = Flask(__name__)
app.config.from_object('config.default')
app.config['SECRET_KEY'] = SECRET_KEY  # Setting the secret key explicitly
mongo = PyMongo(app)