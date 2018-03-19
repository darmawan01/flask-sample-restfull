from flask_jwt_extended import jwt_required
from flask_restful import Resource,reqparse
from models.posts import PostsModel

class NewPost(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument('user',type=str, required=True, help='User Cannot be blank.')
    parse.add_argument('title', type=str, required=True, help='Title Cannot be blank.')
    parse.add_argument('content', type=str, required=True, help='Content Cannot be blank.')
    parse.add_argument('img', type=str, required=True, help='img Cannot be blank.')

    @jwt_required
    def post(self):
        data = NewPost.parse.parse_args()

        if PostsModel.find_by_title(data['title']):
            return {"messages" : "a member with that email already exists"}, 400

        posts_data = PostsModel(data['user'],
                          data['title'],
                          data['content'],
                          data['img'],
                          )

        try:
            posts_data.save_to_db()
        except:
            return {"message": "an error occurred creating the member."}, 500

        return {"message": "member created successfully."}, 201

class Post(Resource):
    parse = reqparse.RequestParser()

    parse.add_argument('user', type=str, required=True, help='User Cannot be blank.')
    parse.add_argument('title', type=str, required=True, help='Title Cannot be blank.')
    parse.add_argument('content', type=str, required=True, help='Content Cannot be blank.')
    parse.add_argument('img', type=str, required=True, help='img Cannot be blank.')

    def get(self, id):

        post_data = PostsModel.find_by_id(id)

        if post_data:
            return post_data.json()
        else:
            return {'message': 'article not found'}, 404

    @jwt_required
    def put(self, id):

        data = Post.parse.parse_args()

        post_data = PostsModel.find_by_id(id)

        if post_data:
            post_data.user = data['user']
            post_data.title = data['title']
            post_data.content = data['content']
            post_data.img = data['img']

            try:
                post_data.save_to_db()
            except:
                return {"message": "an error occurred update the article."}, 500

            return {'message': 'article succes update'}, 200
        else:
            return {'message': 'article not found'}, 404

    @jwt_required
    def delete(self, id):

        post_data = PostsModel.find_by_id(id)

        if post_data:
            try:
                post_data.delete_to_db()
            except:
                return {"message": "an error occurred delete the article."}, 500

            return {'message': 'article succes delete'}, 200
        else:
            return {'message': 'article not found'}, 404

class PostsList(Resource):
    def get(self, count):
        def countx():
            return int(count) * 10

        data = PostsModel.query.all()
        posts = []
        post_page = []

        if not data:
            return {"message": "article not found."}, 200

        else:
            for post in data:
                post_data = {}
                post_data['user'] = post.user
                post_data['title'] = post.title
                post_data['content'] = post.content
                post_data['img'] = post.img
                post_data['created_at'] = str(post.created_at)
                posts.append(post_data)

            if countx() > len(posts) and   len(posts) < countx():
                for s in range((countx() - 10), len(posts)):
                    post_page.append(posts[s])
            else:
                for s in range((countx() - 10), countx()):
                    post_page.append(posts[s])

        return {'articles': post_page,
                'total': len(post_page)}

