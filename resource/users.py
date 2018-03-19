from flask_jwt_extended import jwt_required
from flask_restful import Resource,reqparse
from models.users import UsersModel

class UserRegister(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument('fullName',type=str, required=True, help='Name Cannot be blank.')
    parse.add_argument('email', type=str, required=True, help='Email Cannot be blank.')
    parse.add_argument('username', type=str, required=True, help='Username Cannot be blank.')
    parse.add_argument('password', type=str, required=True, help='Password Cannot be blank.')

    @jwt_required
    def post(self):
        data = UserRegister.parse.parse_args()

        if UsersModel.find_by_email(data['email']):
            return {"messages" : "a member with that email already exists"}, 400

        user_data = UsersModel(data['fullName'],
                          data['email'],
                          data['username'],
                          data['password']
                          )

        try:
            user_data.save_to_db()
        except:
            return {"message": "an error occurred creating the member."}, 500

        return {"message": "member created successfully."}, 201

class User(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument('fullName', type=str, required=True, help='Name Cannot be blank.')
    parse.add_argument('email', type=str, required=True, help='Email Cannot be blank.')
    parse.add_argument('username', type=str, required=True, help='Username Cannot be blank.')
    parse.add_argument('password', type=str, required=True, help='Password Cannot be blank.')

    def get(self, id):
        user_data = UsersModel.find_by_email(id) or UsersModel.find_by_fullName(id)

        if user_data:
            return user_data.json()
        else:
            return {'message': 'member not found'}, 404

    @jwt_required
    def put(self,id):
        data = User.parse.parse_args()

        user_data = UsersModel.find_by_email(id) or UsersModel.find_by_fullName(id)

        if user_data:
            user_data.fullName = data['fullName']
            user_data.email = data['email']
            user_data.username = data['username']
            user_data.password = data['password']

            try:
                UsersModel.save_to_db()
            except:
                return {"message": "an error occurred update the member."}, 500

            return {'message': 'member succes update'}, 200
        else:
            return {'message': 'member not found'}, 404

    @jwt_required
    def delete(self, id):

        member_data = UsersModel.find_by_email(id) or UsersModel.find_by_fullName(id)

        if member_data:
            try:
                UsersModel.delete_to_db()
            except:
                return {"message": "an error occurred update the member."}, 500

            return {'message': 'member succes delete'}, 200
        else:
            return {'message': 'member not found'}, 404