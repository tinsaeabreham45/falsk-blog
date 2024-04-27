import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f0a4d22d29e0f62261cc22a6d714af71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Tinsae Abreham/flask-blog/flaskBlog/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tinsaep777@gmail.com'
app.config['MAIL_PASSWORD'] = 'vuit duua zixv ozov'
mail = Mail(app)
from flaskBlog.users.routes import users
from flaskBlog.posts.routes import posts
from flaskBlog.main.routes import main
from flaskBlog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
cl