from sqlalchemy.exc import IntegrityError
from dals.models import db, Meal


def create_meal(meal_args):
    try:
        new_meal = Meal(**meal_args)
        db.session.add(new_meal)
        db.session.commit()

        return new_meal.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def update_meal(meal_id, meal_patch):
    meal = Meal.get_meal_by_id(meal_id)
    for key, value in meal_patch.items():
        setattr(meal, key, value)


def get_meals_by_account(account_id):
    meals = Meal.query.filter(Meal.account_id == account_id)
    if len(meals.all()) == 0:
        return []
    return [meal.full_view() for meal in meals.all()]


def get_meals_by_date(account_id, date):
    meals = Meal.query.filter(Meal.account_id == account_id, Meal.date_logged == date)
    if len(meals) == 0:
        return []
    return [meal.full_view() for meal in meals.all()]


def get_meals_by_category(account_id, category):
    meals = Meal.query.filter(Meal.account_id == account_id, Meal.category == category)
    if len(meals) == 0:
        return []
    return [meal.full_view() for meal in meals.all()]


def get_meals_by_category_and_date(account_id, category, date):
    meals = Meal.query.filter(
        Meal.account_id == account_id, Meal.category == category, Meal.date_logged == date
    )
    if len(meals) == 0:
        return []
    return [meal.full_view() for meal in meals.all()]