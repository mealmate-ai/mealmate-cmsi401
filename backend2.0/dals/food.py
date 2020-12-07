from sqlalchemy.exc import IntegrityError
from dals.models import db, Food


def insert_food(food_args):
    try:
        inserted_food = Food(**food_args)
        db.session.add(inserted_food)
        db.session.commit()
        return inserted_food.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_food_by_foodid(food_id):
    food = Food.get_food_by_id(food_id)
    return food.full_view()


def get_foods_in_meal(meal_id):
    foods = Food.get_foods_by_meal_id(meal_id)
    return [food.full_view() for food in foods.all()]