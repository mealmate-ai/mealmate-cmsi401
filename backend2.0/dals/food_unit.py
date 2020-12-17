from sqlalchemy.exc import IntegrityError
from dals.models import db, FoodUnit


def insert_food_units(food_units_list):
    try:
        new_units = []
        for food_unit in food_units_list:
            new_unit = FoodUnit(**food_unit)
            new_units.append(new_unit)
            db.session.add(new_unit)
        db.session.commit()
        return [unit.full_view() for unit in new_units]
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
