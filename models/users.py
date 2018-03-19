from datetime import datetime
from core.db import db


class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(20))
    email = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, fullName, email, username, password):
        self.email = email
        self.fullName = fullName
        self.password = password

    @classmethod
    def find_by_fullName(cls, fullName):
        return cls.query.filter_by(fullName=fullName).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # save
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete
    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id': self.nim,
                'fullName': self.fullName,
                'email': self.email,
                'admin': self.admin,
                'created_at': str(self.created_at)
                }