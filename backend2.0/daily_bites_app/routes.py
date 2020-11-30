from flask import g, request
from daily_bites_app import app

import services.account as account_service
import services.meal as meal_service
import services.food as food_service


def parsed_request():
    content = request.get_json()
    print("CONTENT", content, request)
    if content is None:
        return "content parse failed"  # add exception !!
    return content


@app.route("/", methods=["GET"])
def hello():
    return {"message": "Hello"}, 200


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

    print(category, date)
    if category and date:
        return meal_service.get_meals_by_account_date_category(account_id, category, date)
    if category:
        print(category)
        return meal_service.get_meals_by_account_category(account_id, category)
    if date:
        return meal_service.get_meals_by_account_date(account_id, date)

    return meal_service.get_meals_by_account(account_id)


@app.route("/delete-meal/<meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    return meal_service.remove_meal(meal_id)


@app.route("/add-food", methods=["POST"])
def new_food():
    return food_service.create_food(parsed_request())


@app.route("/query-foods", methods=["GET"])
def query_foods():
    # query = request.args.get("query")
    # foods = re.split("\s+|[,]", query)

    # matches = {}
    # items = []
    # for food in foods:
    #     text = food.replace("'", "''")
    #     res = FoodDetail.query.filter(FoodDetail.processed_desc.contains(text)).all()
    #     items += res
    #     matches[text] = [item.food_id for item in res]
    # print(matches, items)
    # # for item in items:
    # #     print(item)

    return "WIP"
