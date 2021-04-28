from flask import g, request
from daily_bites_app import app
from daily_bites_app.errors import BadArgumentError
import services.account as account_service
import services.meal as meal_service
import services.food as food_service
import services.recipe as recipe_service
import services.nutrition as nutrition_service
import services.auth as auth_service
import services.chatbot as chatbot_service
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
    print('start of verification', token)
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
        print('payload', payload)
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
    if 'sub' in payload and 'iat' in payload:
        last_logout = dal.get_last_logout(payload['sub'])
        expire = datetime.fromtimestamp(payload['iat'])
        print('token here', last_logout, expire)
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

@app.route("/meal/<meal_id>", methods=["GET"])
@auth.login_required
def get_meal_details(meal_id):
    # TODO: check that meal id belongs to current user
    return meal_service.meal_full_view(meal_id)

@app.route('/meal/<meal_id>', methods=['PATCH'])
@auth.login_required
def update_meal(meal_id):
    # TODO: think about what users will want to update (specific food items)
    return 'WIP'

@app.route('/recipes', methods=['GET'])
@auth.login_required
def get_recipes():
    number = request.args.get("number")
    n = number if number else 5
    return recipe_service.get_filtered_recipes(g.user, n)

@app.route("/save-recipe/<recipe_id>", methods=["POST"])
@auth.login_required
def create_saved_recipe(recipe_id):
    return recipe_service.save_recipe(g.user, recipe_id)


@app.route('/my-recipes', methods=['GET'])
@auth.login_required
def get_my_recipes():
    return recipe_service.recipes_list(g.user)

@app.route('/saved-recipes', methods=['GET'])
@auth.login_required
def get_saved_recipes():
    return recipe_service.bulk_recipe_lookup(g.user)

@app.route('/recipe/<recipe_id>', methods=['GET'])
@auth.login_required
def get_recipe_details(recipe_id):
    return recipe_service.recipe_details(recipe_id)


@app.route('/chatbot/create-meal', methods=['POST'])
@auth.login_required
def chatbot():
    return chatbot_service.tag_and_create_meal(g.user, parsed_request())