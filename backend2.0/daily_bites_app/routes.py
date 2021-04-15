# from flask import g, request
# from daily_bites_app import app
# from daily_bites_app.errors import BadArgumentError
# import services.account as account_service
# import services.meal as meal_service
# import services.food as food_service
# import services.recipe as recipe_service
# import services.nutrition as nutrition_service
# import services.auth as auth_service
# from flask_httpauth import HTTPTokenAuth
# import jwt
# import os

# auth = HTTPTokenAuth(scheme='Bearer')


# @auth.error_handler
# def token_error():
#     return {'message': 'Invalid Token'}, 401


# @auth.verify_token
# def verify_token(token):
#     try:
#         payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
#         return payload['sub']
#     except jwt.ExpiredSignatureError:
#         return 'Signature expired. Please log in again.'
#     except jwt.InvalidTokenError:
#         return 'Invalid token. Please log in again.'


# def parsed_request():
#     content = request.get_json()
#     if content is None:
#         raise BadArgumentError("Error occured when parsing arguments")
#     return content


# @app.route("/", methods=["GET"])
# def hello():
#     return {"message": "Welcome to the Daily Bites Flask Server!"}, 200


# @app.route("/signup", methods=["POST"])
# def signup():
#     return account_service.signup(parsed_request())


# @app.route("/login", methods=["POST"])
# def login():
#     return account_service.login(parsed_request())


# # TODO: Need to check if this is still up to date
# # TODO: detect user based on auth token
# # get user from token!!

# @app.route('/update-account', methods=["PATCH"])
# @auth.login_required
# def update_account():
#     return account_service.update_account(parsed_request())


# @app.route('/request-password-reset', methods=["POST"])
# def request_password_update():
#     """ TODO: figure out how to handle password reset requests, need to add new table! """
#     return "TODO"


# @app.route('/request-password-reset/<key>', methods=['POST'])
# def change_password(key):
#     """ TODO: get key from prev route """
#     return "TODO"


# @app.route('/user-details', methods=["GET"])
# @auth.login_required
# def get_user_details():
#     """
#     TODO: get current user's details using token
#     """
#     return "TODO"


# # TODO: add period param to endpoint to allow for filtering
# @app.route('/nutrition', methods=["GET"])
# @auth.login_required
# def get_nutrition():
#     return "TODO"


# @app.route('/create-meal', methods=["GET"])
# @auth.login_required
# def create_meal_from_chatbot():
#     """
#     TODO: create method that tags item using raw_text
#     TODO: tell Adriana she needs to send token too
#     """
#     return "TODO"


# # TODO: add meal creation for food item
# # TODO: figure out what to do for meal log

# @app.route('/barcode/<barcode>', methods=["POST"])
# @auth.login_required
# def create_meal_from_barcode():
#     return "TODO"


# @app.route('/get-meal-details', methods=["GET"])
# @auth.login_required
# def get_meal_details():
#     return "TODO"


# @app.route('/update-meal-item/<meal_id>/<food_id>', methods=["PATCH"])
# @auth.login_required
# def update_meal(meal_id, food_id):
#     return "TODO"


# @app.route('/get-recipes', methods=["GET"])
# @auth.login_required
# def get_recipes():
#     return "GET FROM ROUTES.PY"


# @app.route('/save-recipe', methods=["POST"])
# @auth.login_required
# def save_recipe():
#     return True
