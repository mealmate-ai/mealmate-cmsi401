from flask import g
from daily_bites_app import app


@app.route("/", methods=["GET"])
def hello():
    return {"message": "Hello"}, 200


@app.route("/add-account", methods=["GET"])
def new_account():
    # id = request.args.get("id")
    # date_created = datetime.today().strftime("%Y-%m-%d")
    # email = request.args.get("email", None)
    # name = request.args.get("name", None)

    # account = Account(id, date_created, name, email, "", "", "", "")
    # db.session.add(account)
    # db.session.commit()

    return "WIP"


@app.route("/update-account/<account_id>", methods=["GET"])
def update_account(account_id):
    # name = request.args.get("name", None)
    # email = request.args.get("email", None)

    # account_updating = db.session.query(Account).filter_by(id=account_id).first()
    # account_updating.name = name if name else account_updating.name
    # account_updating.email = email if email else account_updating.email

    # db.session.commit()
    return "WIP"


@app.route("/delete-account/<account_id>", methods=["DELETE"])
def update_account(account_id):
    return "WIP"


@app.route("/add-meal/<account_id>", methods=["GET"])
def new_meal(account_id):
    # account_id = request.args.get("accountId")
    # date_logged = datetime.today().strftime("%Y-%m-%d")
    # category = request.args.get("category")

    # meal_new = Meal(None, account_id, date_logged, category)
    # db.session.add(meal_new)
    # db.session.commit()

    return "WIP"


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
