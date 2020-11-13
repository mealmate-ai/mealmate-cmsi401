from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db_models import Account

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
    id = request.args.get('id')
    date_created = datetime.today().strftime('%Y-%m-%d')
    email = request.args.get('email', None)
    name = request.args.get('name', None)
  
    new_account = Account(id, date_created, name, email)
    db.session.add(new_account)
    db.session.commit()

    return 'New Account {0}, {1}'.format(new_account.id, new_account.name)

@app.route('/update-account/<account_id>', methods=['GET'])
def update_account(account_id):
    name = request.args.get('name', None)
    
    account_updating = db.session.query(Account).filter_by(id = account_id).first()
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