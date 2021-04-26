from sqlalchemy.exc import IntegrityError
from dals.models import db, Nutrition, Meal, Food, TotalNutritionView
from datetime import datetime
from sqlalchemy import func, text


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

def get_user_nut(account_id, period):
    foods = []
    if period == 'day':
        foods = Meal.query.join(Food, Food.meal_id == Meal.id).join(TotalNutritionView, TotalNutritionView.food_id == Food.food_id).filter(Meal.account_id == account_id, Meal.date_logged == datetime.today().strftime("%Y-%m-%d"))
    if period == 'week':
        foods = Meal.query.join(Food, Food.meal_id == Meal.id).join(TotalNutritionView, TotalNutritionView.food_id == Food.food_id).filter(Meal.account_id == account_id, Meal.date_logged >= (func.date_sub(func.now(),  text('INTERVAL  1 WEEK'))))
    if period == 'month':
        foods = Meal.query.join(Food, Food.meal_id == Meal.id).join(TotalNutritionView, TotalNutritionView.food_id == Food.food_id).filter(Meal.account_id == account_id, Meal.date_logged >= (func.date_sub(func.now(),  text('INTERVAL  1 MONTH'))))
    
    print('FOODS ', foods)
    total_cal = 0
    total_carb = 0
    total_fat = 0
    total_prot = 0
    # for food in foods:
    #     mult = 1.0 # float(quantity) * float(food_unit / 100.0)
    #     total_cal += mult * food[3]
    #     total_prot += mult * food[4]
    #     total_fat += mult * food[5]
    #     total_carb += mult * food[6]

    return {
        'period': period,
        'calories': total_cal,
        'fat': total_fat,
        'protein': total_prot,
        'carbs': total_carb
    }