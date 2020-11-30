from sqlalchemy.exc import IntegrityError
from dals.models import db, Recipe


def insert_spoonacular_recipe(recipe_details):
    try:
        inserted_recipe = Recipe(**recipe_details)
        db.session.add(inserted_recipe)
        db.session.commit()

        return inserted_recipe.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_recipe(recipe_id):
    recipe = Recipe.get_recipe_by_id(recipe_id)

    return recipe.full_view()