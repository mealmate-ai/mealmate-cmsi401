from sqlalchemy.exc import IntegrityError
from dals.models import db, Nutrition


def insert_nut_food(food_args):
    try:
        new_food = Nutrition(**food_args)
        db.session.add(new_food)
        db.session.commit()

        return new_food.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_nut_food_by_id(food_id):
    food = Nutrition.get_food_by_id(food_id)

    return food.full_view()