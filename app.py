from urllib import request
from flask import Flask
from database import Database

app = Flask(__name__)
db = Database()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
