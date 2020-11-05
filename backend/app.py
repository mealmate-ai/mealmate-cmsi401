from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/postgres'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/get-account', methods=['GET'])
def new_route():
    user_id = request.args.get('user_id')
    return user_id

@app.route('/add-account', methods=['GET'])
def new_account():
    name = request.args.get('name', None)
    email = request.args.get('email', None)
    fbid = request.args.get('fbid')

    return name + fbid + email


if __name__ == '__main__':
    app.debug = True
    app.run()