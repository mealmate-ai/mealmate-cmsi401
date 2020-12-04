from services import dal
from checks import MealChecker, MealLogChecker
from datetime import datetime
import uuid
from dals.models import Meal


def create_meal(account_id, meal_info):
    meal = MealChecker.__on_creation__(meal_info)
    meal["id"] = uuid.uuid4()
    meal["account_id"] = account_id
    meal["date_logged"] = datetime.today().strftime("%Y-%m-%d")
    return {"meal": dal.create_meal(meal)}, 201


def get_meals_by_account(account_id):
    # check valid account_id ?
    meals = dal.get_meals_by_account(account_id)
    return {"meals": meals}, 200


def get_meals_by_account_date(account_id, date):
    meals = dal.get_meals_by_date(account_id, date)
    return {"meals": meals}, 200


def get_meals_by_account_category(account_id, category):
    meals = dal.get_meals_by_category(account_id, category)
    return {"meals": meals}, 200


def get_meals_by_account_date_category(account_id, category, date):
    meals = dal.get_meals_by_category_and_date(account_id, category, date)
    return {"meals": meals}, 200


def remove_meal(meal_id):
    return {"deleted": dal.delete_meal(meal_id)}, 200


def log_meal(meal_id, meal_log_info):
    meal_log = MealLogChecker.__on_creation__(meal_log_info)
    meal_log["meal_id"] = meal_id
    print('MEAL LOG', meal_log)

    return {"meal_log": dal.insert_meal_log(meal_log)}, 201
