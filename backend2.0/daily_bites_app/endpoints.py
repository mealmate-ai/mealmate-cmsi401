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
import jwt
import os

auth = HTTPTokenAuth(scheme='Bearer')


@auth.error_handler
def token_error():
    return {'message': 'Invalid Token'}, 401


@auth.verify_token
def verify_token(token):
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return {'message': 'Signature expired. Please log in again.'}, 400
    except jwt.InvalidTokenError:
        return {'message': 'Invalid token. Please log in again.'}, 401


def parsed_request():
    content = request.get_json()
    if content is None:
        raise BadArgumentError("Error occured when parsing arguments")
    return content


@app.route("/", methods=["GET"])
@auth.verify_token
def hello():
    return {"message": "Welcome to the Daily Bites Flask Server!"}, 200


@app.route("/signup", methods=["POST"])
def signup():
    return account_service.signup(parsed_request())


@app.route("/login", methods=["POST"])
def login():
    return account_service.login(parsed_request())
