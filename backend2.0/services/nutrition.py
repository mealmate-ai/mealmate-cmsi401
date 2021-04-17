from services import dal
from checks import MealChecker, MealLogChecker
from datetime import datetime
import uuid
from dals.models import Meal


def get_nutrition_by_date(account_id, date_logged):
    meals = dal.get_meals_by_date(account_id, date_logged)
    # get meals in date range

    nutrition = {}
    for meal in meals:
        print(meal)

    return {nutrition}, 200
    