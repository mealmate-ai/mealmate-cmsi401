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
