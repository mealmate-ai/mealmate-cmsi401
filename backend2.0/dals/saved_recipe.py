from sqlalchemy.exc import IntegrityError
from dals.models import db, SavedRecipe, Recipe


def insert_saved_recipe(recipe_details):
    try:
        new_saved_recipe = SavedRecipe(**recipe_details)
        db.session.add(new_saved_recipe)
        db.session.commit()

        return new_saved_recipe.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_recipes_list(account_id):
    recipes = SavedRecipe.get_saved_recipes_by_user(account_id)
    return [Recipe.get_recipe_by_id(recipe[0]).full_view() for recipe in recipes]