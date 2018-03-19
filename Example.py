from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config.database import Configuration

from resource.index import Auth,Index
from resource.users import User, UserRegister
from resource.posts import Post, NewPost, PostsList

app = Flask(__name__)

app.config.from_object(Configuration)

jwt = JWTManager(app)
api = Api(app)

# endpoint Auth
api.add_resource(Index, '/')
api.add_resource(Auth, '/auth')

# endpoint of User
api.add_resource(UserRegister, '/user')
api.add_resource(User, '/user/<string:email>')


# endpoint of Post
api.add_resource(NewPost, '/post')
api.add_resource(Post, '/post/<int:id>')
api.add_resource(PostsList, '/post/list/<int:count>')

if __name__ == '__main__':
    from core.db import db

    db.init_app(app)
    app.run()