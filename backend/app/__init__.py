from flask import Flask
from pymongo import MongoClient
from app.config import Config
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)

#enable CORS for all routes
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

#mongoDB connection
client = MongoClient(app.config["MONGO_URI"])
db = client.get_database()

#import routes
from app.routes.auth import auth_bp
from app.routes.chatbot import chatbot_bp
app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)

from app.routes.socket import *