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
#         raise BadArgumentError("Error on parsing arguments")
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

# # DEPRECATED - DON'T USE
# @app.route("/add-account", methods=["POST"])
# @auth.login_required
# def create_account():
#     return account_service.create_account(parsed_request())


# @app.route("/get-account/<account_id>", methods=["GET"])
# @auth.login_required
# @auth_service.token_required
# def get_account(account_id):
#     return account_service.get_account(account_id)


# @app.route("/update-account/<account_id>", methods=["PATCH"])
# @auth.login_required
# def update_account(account_id):
#     return account_service.update_account(account_id, parsed_request())


# @app.route("/delete-account/<account_id>", methods=["DELETE"])
# @auth.login_required
# def delete_account(account_id):
#     return account_service.remove_account(account_id)


# @app.route("/add-meal/<account_id>", methods=["POST"])
# @auth.login_required
# def new_meal(account_id):
#     return meal_service.create_meal(account_id, parsed_request())


# @app.route("/get-meal/<account_id>", methods=["GET"])
# @auth.login_required
# def get_meal(account_id):
#     date = request.args.get("date")
#     category = request.args.get("category")

#     if category and date:
#         return meal_service.get_meals_by_account_date_category(account_id, category, date)
#     if category:
#         return meal_service.get_meals_by_account_category(account_id, category)
#     if date:
#         return meal_service.get_meals_by_account_date(account_id, date)

#     return meal_service.get_meals_by_account(account_id)


# @app.route("/delete-meal/<meal_id>", methods=["DELETE"])
# @auth.login_required
# def delete_meal(meal_id):
#     return meal_service.remove_meal(meal_id)


# # might remove this endpoint, won't be calling nutritionix api from frontend currently
# @app.route("/add-food", methods=["POST"])
# @auth.login_required
# def new_food():
#     return food_service.create_food(parsed_request())


# @app.route("/query-foods", methods=["GET"])
# @auth.login_required
# def query_foods():
#     query = request.args.get("query")
#     return food_service.search_foods(query)


# @app.route("/query-mv-foods", methods=["GET"])
# @auth.login_required
# def query_mv_foods():
#     query = request.args.get("query")
#     return food_service.search_mat_view_foods(query)


# @app.route("/query-barcode/<barcode>", methods=["GET"])
# @auth.login_required
# def query_barcode(barcode):
#     return food_service.get_by_barcode(barcode)


# @app.route("/get-nutrition/<account_id>", methods=["GET"])
# @auth.login_required
# def get_nutrition(account_id):
#     date_logged = request.args.get("dateLogged")
#     return nutrition_service.get_nutrition_by_date(account_id, date_logged)


# @app.route("/log-meal/<meal_id>", methods=["POST"])
# @auth.login_required
# def log_meal(meal_id):
#     return meal_service.log_meal(meal_id, parsed_request())


# # CONSULT W/ MAYA
# @app.route("/insert-recipe", methods=["POST"])
# @auth.login_required
# def create_recipe():
#     return 'TODO'

# # GET SPECIFIC RECIPE by ID 
# @app.route("/get-recipe/<recipe_id>", methods=["GET"])
# @auth.login_required
# def get_recipe(recipe_id):
#     return 'TODO'

# # GET RECOMMENDED RECIPES w/ USER INFO
# @app.route("/get-recipes/<account_id>", methods=["GET"])
# @auth.login_required
# def get_tailored_recipes(account_id):
#     number = request.args.get("number")
#     n = number if number else 5
#     return recipe_service.get_filtered_recipes(account_id, n)


# @app.route("/get-random-recipes", methods=["GET"])
# @auth.login_required
# def get_random_recipes():
#     number = request.args.get("number")
#     n = number if number else 5
#     return recipe_service.get_random_recipes(n)


# @app.route("/get-recipe-ingredients/<recipe_id>", methods=["GET"])
# @auth.login_required
# def get_recipe_ingredients(recipe_id):
#     return recipe_service.get_recipe_ingredients(recipe_id)


# @app.route("/get-recipe-instructions/<recipe_id>", methods=["GET"])
# @auth.login_required
# def get_recipe_instructions(recipe_id):
#     return recipe_service.get_recipe_instructions(recipe_id)


# @app.route("/get-recipe-nutrition/<recipe_id>", methods=["GET"])
# @auth.login_required
# def get_recipe_nutrition(recipe_id):
#     return recipe_service.get_recipe_nutrition(recipe_id)


# @app.route("/save-recipe/<account_id>", methods=["POST"])
# @auth.login_required
# def create_saved_recipe(account_id):
#     return 'TODO'


# @app.route("/get-saved-recipes/<account_id>", methods=["GET"])
# @auth.login_required
# def get_saved_recipes(account_id):
#     return 'TODO'
