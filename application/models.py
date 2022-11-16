from application import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pwd_hashed = db.Column(db.String(128))
    profilepic = db.Column(db.String(250))
    aboutme = db.Column(db.Text())
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'{self.username}'

    def hash_pwd(self, password):
        self.pwd_hashed = generate_password_hash(password)

    def check_pwd(self, password):
        return check_password_hash(self.pwd_hashed, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    pic = db.Column(db.String(250))
    body = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'{self.title}'
