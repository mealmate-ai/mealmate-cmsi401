from sqlalchemy.sql import func, and_, or_
from sqlalchemy.exc import IntegrityError
from dals.models import db, FoodDetail, TotalNutritionView


def insert_food_detail(food_detail_args):
    try:
        inserted_food_detail = FoodDetail(**food_detail_args)
        db.session.add(inserted_food_detail)
        db.session.commit()
        return inserted_food_detail.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_food_detail(food_id):
    food = FoodDetail.get_food_detail_by_id(food_id)
    return food.full_view()


def search_foods(search_query):
    query = FoodDetail.query.filter(
        func.to_tsvector("english", FoodDetail.food_desc).op("@@")(
            func.plainto_tsquery("english", search_query)
        )
    )
    foods = [food.search_result_view() for food in query.all()]
    return foods


def search_mv_foods(search_query):
    # https://stackoverflow.com/questions/33025891/returning-ranked-search-results-using-gin-index-with-sqlalchemy
    query = TotalNutritionView.query.filter(
        func.to_tsvector("english", TotalNutritionView.food_desc).op("@@")(
            func.plainto_tsquery("english", search_query)
        )
    )
    foods = [food.search_result_view() for food in query.all()]
    return foods
