from sqlalchemy.sql import func, and_, or_
from sqlalchemy.exc import IntegrityError
from dals.models import db, TotalNutritionView


def get_food_by_barcode(barcode):
    food = TotalNutritionView.get_food_by_barcode(barcode)
    return food.full_view()
