from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/postgres'
db = SQLAlchemy(app)

ACCOUNT_TABLE = "account"

class Account(db.Model):
    __tablename__ = ACCOUNT_TABLE

    id = db.Column(db.Text, primary_key = True)
    date_created = db.Column(db.Date, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, id, date_created, name, email):
      self.id = id
      self.date_created = date_created
      self.name = name
      self.email = email

    def __repr__(self):
        return '<account_id {0}, name {1}>'.format(self.id, self.name)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/get-account', methods=['GET'])
def new_route():
    user_id = request.args.get('user_id')
    return user_id

@app.route('/add-account', methods=['GET'])
def new_account():
    id = request.args.get('id')
    date_created = datetime.today().strftime('%Y-%m-%d')
    email = request.args.get('email', None)
    name = request.args.get('name', None)
  
    new_account = Account(id, date_created, name, email)
    db.session.add(new_account)
    db.session.commit()

    return 'New Account'

@app.route('/update-account', methods=['GET'])
def update_account():
    id = request.args.get('id')
    name = request.args.get('name', None)
    
    account_updating = Account.query.filter_by(id = id).first()
    account_updating.name = name

    db.session.commit()
    return 'Updated Account'

# @app.route('/get-nut', methods=['GET'])
# def nut():
#     account_id = request.args.get('account_id', None)
#     date = request.args.get('date', None)
#     calc_nut(account_id, date)

if __name__ == '__main__':
    app.debug = True
    app.run()