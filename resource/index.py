from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

from models.users import UsersModel

class Index(Resource):
    def get(self):
        return "Blank Page !!"

class Auth(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument('username',type=str, required=True, help='Username cannot be null.')
    parse.add_argument('password',type=str, required=True, help='Password cannot be null.')

    def post(self):
        data = Auth.parse.parse_args()

        isAdmin = UsersModel.find_by_username(data['username'])
        user = UsersModel.find_by_username(data['username'])

        if isAdmin and isAdmin.admin is True:
            if isAdmin and safe_str_cmp(isAdmin.password, data['password']):
                return {'token': create_access_token(identity=data['username'])}, 200 #basic ascces token
            else:
                return {"message": "Bad username or password."}, 201
        elif user:
            if user and safe_str_cmp(user.password, data['password']):
                return {'token': create_access_token(identity=data['username'])}, 200 #basic ascces token
            else:
                return {"message": "Bad username or password."}, 201
