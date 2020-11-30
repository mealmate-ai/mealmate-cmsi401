from sqlalchemy.exc import IntegrityError
from dals.models import db, MealLog


def insert_meal_log(meal_log_args):
    try:
        inserted_meal_log = MealLog(**meal_log_args)
        db.session.add(inserted_meal_log)
        db.session.commit()

        return inserted_meal_log.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise
