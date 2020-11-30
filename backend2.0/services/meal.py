from services import dal
from checks import MealChecker
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
