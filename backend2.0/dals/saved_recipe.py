from sqlalchemy.exc import IntegrityError
from dals.models import db, SavedRecipe


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


def get_recipes(account_id):
    recipes = SavedRecipe.get_saved_recipes_by_user(account_id)

    return [recipe.full_view() for recipe in recipes.all()]