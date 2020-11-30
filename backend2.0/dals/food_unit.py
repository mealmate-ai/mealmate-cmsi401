from sqlalchemy.exc import IntegrityError
from dals.models import db, FoodUnit


def insert_food_unit(food_unit_args):
    try:
        new_unit = FoodUnit(**food_unit_args)
        db.session.add(new_unit)
        db.session.commit()
        return new_unit.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_food_units(food_id):
    units = FoodUnit.get_all_units_by_id(food_id)

    return [unit.full_view() for unit in units.all()]


def get_food_by_unit(food_id, unit, desc):
    unit = FoodUnit.get_all_units_by_id(food_id)

    return unit.full_view()
