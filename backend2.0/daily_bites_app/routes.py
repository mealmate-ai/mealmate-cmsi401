from flask import g, request
from daily_bites_app import app
from daily_bites_app.errors import BadArgumentError
import services.account as account_service
import services.meal as meal_service
import services.food as food_service
import services.recipe as recipe_service
import services.nutrition as nutrition_service


def parsed_request():
    content = request.get_json()
    if content is None:
        raise BadArgumentError("Error on parsing arguments")
    return content


@app.route("/", methods=["GET"])
def hello():
    return {"message": "Hello"}, 200


@app.route("/signup", methods=["POST"])
def signup():
    return account_service.signup(parsed_request())


@app.route("/add-account", methods=["POST"])
def create_account():
    return account_service.create_account(parsed_request())


@app.route("/get-account/<account_id>", methods=["GET"])
def get_account(account_id):
    return account_service.get_account(account_id)


@app.route("/update-account/<account_id>", methods=["PATCH"])
def update_account(account_id):
    return account_service.update_account(account_id, parsed_request())


@app.route("/delete-account/<account_id>", methods=["DELETE"])
def delete_account(account_id):
    return account_service.remove_account(account_id)


@app.route("/add-meal/<account_id>", methods=["POST"])
def new_meal(account_id):
    return meal_service.create_meal(account_id, parsed_request())


@app.route("/get-meal/<account_id>", methods=["GET"])
def get_meal(account_id):
    date = request.args.get("date")
    category = request.args.get("category")

    if category and date:
        return meal_service.get_meals_by_account_date_category(account_id, category, date)
    if category:
        return meal_service.get_meals_by_account_category(account_id, category)
    if date:
        return meal_service.get_meals_by_account_date(account_id, date)

    return meal_service.get_meals_by_account(account_id)


@app.route("/delete-meal/<meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    return meal_service.remove_meal(meal_id)


# might remove this endpoint, won't be calling nutritionix api from frontend currently
@app.route("/add-food", methods=["POST"])
def new_food():
    return food_service.create_food(parsed_request())


@app.route("/query-foods", methods=["GET"])
def query_foods():
    query = request.args.get("query")
    return food_service.search_foods(query)


@app.route("/query-mv-foods", methods=["GET"])
def query_mv_foods():
    query = request.args.get("query")
    return food_service.search_mat_view_foods(query)


@app.route("/query-barcode/<barcode>", methods=["GET"])
def query_barcode(barcode):
    return food_service.get_by_barcode(barcode)


@app.route("/get-nutrition/<account_id>", methods=["GET"])
def get_nutrition(account_id):
    date_logged = request.args.get("dateLogged")
    return nutrition_service.get_nutrition_by_date(account_id, date_logged)


@app.route("/log-meal/<meal_id>", methods=["POST"])
def log_meal(meal_id):
    return meal_service.log_meal(meal_id, parsed_request())


# CONSULT W/ MAYA
@app.route("/insert-recipe", methods=["POST"])
def create_recipe():
    return 'TODO'

# GET SPECIFIC RECIPE by ID 
@app.route("/get-recipe/<recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    return 'TODO'

# GET RECOMMENDED RECIPES w/ USER INFO
@app.route("/get-recipes/<account_id>", methods=["GET"])
def get_tailored_recipes(account_id):
    number = request.args.get("number")
    n = number if number else 5
    return recipe_service.get_filtered_recipes(account_id, n)


@app.route("/get-random-recipes", methods=["GET"])
def get_random_recipes():
    number = request.args.get("number")
    n = number if number else 5
    return recipe_service.get_random_recipes(n)


@app.route("/get-recipe-ingredients/<recipe_id>", methods=["GET"])
def get_recipe_ingredients(recipe_id):
    return recipe_service.get_recipe_ingredients(recipe_id)


@app.route("/get-recipe-instructions/<recipe_id>", methods=["GET"])
def get_recipe_instructions(recipe_id):
    return recipe_service.get_recipe_instructions(recipe_id)


@app.route("/get-recipe-nutrition/<recipe_id>", methods=["GET"])
def get_recipe_nutrition(recipe_id):
    return recipe_service.get_recipe_nutrition(recipe_id)


@app.route("/save-recipe/<account_id>", methods=["POST"])
def create_saved_recipe(account_id):
    return 'TODO'


@app.route("/get-saved-recipes/<account_id>", methods=["GET"])
def get_saved_recipes(account_id):
    return 'TODO'
