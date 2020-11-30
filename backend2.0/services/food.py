from services import dal
from checks import NutritionChecker, FoodDetailChecker, FoodUnitChecker
from datetime import datetime
import uuid
from dals.models import Nutrition, FoodDetail, FoodUnit


def create_food(food_info):
    nutrition = NutritionChecker.__on_creation__(food_info["nutrition"], food_info["food_id"])
    food_detail = FoodDetailChecker.__on_creation__(food_info["food_detail"], food_info["food_id"])
    food_units = [
        FoodUnitChecker.__on_creation__(unit, food_info["food_id"])
        for unit in food_info["food_units"]
    ]
    return {
        "nutrition": dal.insert_nut_food(nutrition),
        "food_detail": dal.insert_food_detail(food_detail),
        "food_units": dal.insert_food_units(food_units),
    }, 201


def search_foods(query):
    foods = dal.search_foods(query)
    return {"foods": foods}, 201
