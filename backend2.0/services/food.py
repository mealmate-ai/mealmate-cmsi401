from services import dal
from checks import NutritionChecker
from datetime import datetime
import uuid
from dals.models import Nutrition, FoodDetail, FoodUnit


def create_food(food_info):
    print(food_info["nutrition"], food_info["food_detail"], food_info["food_id"])
    nutrition = NutritionChecker.__on_creation__(food_info)

    return {"nutrition": dal.insert_food(nutrition)}, 201
