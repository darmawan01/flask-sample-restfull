from core.db import db
from datetime import  datetime

class PostsModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50))
    content = db.Column(db.TEXT)
    img = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, user, title, content, img):
        self.user = user
        self.title = title
        self.content = content
        self.img = img


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(user=id).first()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    # save
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # delete
    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id': self.id,
                'user': self.user,
                'title': self.title,
                'content': self.content,
                'img': self.img,
                'created_at': str(self.created_at)}