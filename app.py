from urllib import request
from flask import Flask
from database import Database

app = Flask(__name__)
db = Database()
api = Api(app)

@app.get('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.post('/register')
def register():
    try:
        email = request.json["email"]
        password = request.json["password"]
    except KeyError:
        return 'Missing parameters'

    return db.create_user(email, password)

@app.post('/login')
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]
    except KeyError:
        return 'Missing parameters'

class Todos():
    def post(self):
        try:
            user_id = request.json["user_id"]
            content = request.json["content"]
        except KeyError:
            return 'Missing parameters'
        return db.add_totos(user_id,content)

    def get(self):
        try:
            user_id = request.json["user_id"]
        except KeyError:
            return 'Missing parameters'
        return db.get_totos(user_id)

api.add_ressource(Todos, "/todos")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)