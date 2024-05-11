from flask import Flask
from flask_mysqldb import MySQL
from config import Config

# create flask app
app = Flask(__name__)
app.config.from_object(Config)

# initialize extensions
mysql = MySQL(app)

# 블루프린트 등록
from app.routes import classification_routes, chatbot_routes, get_trash_data_routes
app.register_blueprint(classification_routes)
app.register_blueprint(chatbot_routes)
app.register_blueprint(get_trash_data_routes)