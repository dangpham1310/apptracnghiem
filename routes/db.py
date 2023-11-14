from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lophoc = db.Column(db.String)
    socau = db.Column(db.String)
    time = db.Column(db.String)
    code = db.Column(db.String(50), unique=False, nullable=False)

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=False, nullable=False)
    def __repr__(self):
        return '<Code %r>' % self.id

