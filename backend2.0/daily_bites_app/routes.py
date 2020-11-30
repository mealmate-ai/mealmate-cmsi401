from flask import g, request
from daily_bites_app import app

import services.account as account_service
import services.meal as meal_service


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
    return "WIP"


@app.route("/delete-meal/<account_id>", methods=["GET"])
def delete_meal(account_id):
    return "WIP"


# # How to query from db? Where do we use nutritionix and where usda db?
@app.route("/add-food-nut/<food_id>", methods=["GET"])
def new_nut(food_id):
    #     kcal = request.args.get("kcal")
    #     protein_g = request.args.get("prot")
    #     total_fat_g = request.args.get("fat")
    #     total_carb_g = request.args.get("carb")

    #     new_nut_food = Nutrition(food_id, kcal, protein_g, total_fat_g, total_carb_g)
    #     db.session.add(new_nut_food)
    #     db.session.commit()

    return "WIP"


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
