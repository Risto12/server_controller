from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from datetime import datetime

db = SQLAlchemy()
login = LoginManager()


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255), unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = self.great_hash(password)

    @staticmethod
    def great_hash(password):
        return generate_password_hash(password)

    def compare_hashes(self, input_password):
        return check_password_hash(self.password, input_password)

    def __repr__(self):
        return '<status {}>'.format(self.status)


class AuthLog(db.Model):

    LOG_TYPES = ("Failure", "Success")

    id = db.Column(db.Integer, primary_key=True)
    log_time = db.Column(db.DateTime(), default=datetime.now())
    status = db.Column(db.String(64))
    ip = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), nullable=True)

    def __init__(self, status, username, ip=None):
        self.status = status
        self.username = username
        self.ip = ip

class Service(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    updated = db.Column(db.DateTime(), default=datetime.now())
    status = db.Column(db.Boolean, nullable=True)
    admin = db.Column(db.Boolean, nullable=False)
    domain = db.Column(db.String(64), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    github = db.Column(db.String(64), nullable=True)


    def __init__(self, name, status, port, domain, admin=False, description=None, github=None):
        self.name = name
        self.status = status
        self.port = port
        self.admin = admin
        self.description = description
        self.github = github
        self.domain = domain


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

