from services import dal
from checks import NutritionChecker, FoodDetailChecker, FoodUnitChecker
from datetime import datetime
import uuid
from dals.models import Nutrition, FoodDetail, FoodUnit
from apis.nutritionix import nutritionix


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


def search_mat_view_foods(query):
    foods = dal.search_mv_foods(query)
    return {"foods": foods}, 201


def get_by_barcode(barcode):
    food = dal.get_food_by_barcode(barcode)

    if not food:
        new_food = nutritionix.barcode_to_food(barcode)
        new_food['food_id'] = 'n' + new_food['food_detail']['barcode']
        return create_food(new_food)

    return {'food': food.full_view()}, 201