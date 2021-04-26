from flask import g, request
from daily_bites_app import app
from daily_bites_app.errors import BadArgumentError
import services.account as account_service
import services.meal as meal_service
import services.food as food_service
import services.recipe as recipe_service
import services.nutrition as nutrition_service
import services.auth as auth_service
from flask_httpauth import HTTPTokenAuth
from services import dal
import jwt
import os
from datetime import datetime

auth = HTTPTokenAuth(scheme='Bearer')


@auth.error_handler
def token_error():
    return {'message': 'Invalid Token'}, 401


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
    if 'sub' in payload and 'iat' in payload:
        last_logout = dal.get_last_logout(payload['sub'])
        expire = datetime.fromtimestamp(payload['iat'])
        print(last_logout, expire)
        if last_logout is None or last_logout < expire:
            g.user = payload['sub']
            return True
    return False


def parsed_request():
    content = request.get_json()
    if content is None:
        raise BadArgumentError("Error occured when parsing arguments")
    return content


@app.route("/", methods=["GET"])
def hello():
    return {"message": "Welcome to the Daily Bites Flask Server!"}, 200


@app.route("/signup", methods=["POST"])
def signup():
    return account_service.signup(parsed_request())


@app.route("/login", methods=["POST"])
def login():
    return account_service.login(parsed_request())


@app.route('/token/refresh', methods=["POST"])
@auth.login_required
def get_new_token():
    return account_service.generate_token(g.user)


@app.route('/logout', methods=["DELETE"])
@auth.login_required
def logout():
    return account_service.logout(g.user)


@app.route("/update-account", methods=["PATCH"])
@auth.login_required
def update_account():
    return account_service.update_account(g.user, parsed_request())


@app.route('/settings/me', methods=["GET"])
@auth.login_required
def account_details():
    return account_service.get_account(g.user)


@app.route("/nutrition", methods=["GET"])
@auth.login_required
def nutrition():
    period = request.args.get("period")
    if period not in ['day', 'week', 'month']:
        return BadArgumentError("Invalid period provided")
    return nutrition_service.calculate_nutrition(g.user, period)