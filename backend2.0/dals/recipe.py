from sqlalchemy.exc import IntegrityError
from dals.models import db, Recipe
from apis.spoonacular import spoonacular

def insert_spoonacular_recipe(recipe_id):
    try:
        recipe = {}
        recipe_info = spoonacular.recipe_information(recipe_id)
        recipe['recipe_id'] = recipe_id
        recipe['title'] = recipe_info['title']
        recipe['recipe_desc'] = recipe_info['summary']
        recipe['image'] = recipe_info['image']
        recipe['dish_type'] = ''.join(recipe_info['dishTypes'])

        inserted_recipe = Recipe(**recipe)
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

def get_recipe_details(recipe_id):
    try:
        recipe = {}
        recipe_info = spoonacular.recipe_information(recipe_id, True)
        print(recipe_info)
        recipe['recipe_id'] = recipe_id
        recipe['title'] = recipe_info['title']
        recipe['recipe_desc'] = recipe_info['summary']
        recipe['image'] = recipe_info['image']
        recipe['dish_type'] = ', '.join(recipe_info['dishTypes'])
        recipe['instructions'] = recipe_info['instructions']
        recipe['cuisines'] = recipe_info['cuisines']
        recipe['nutrition'] = recipe_info['nutrition']
        return recipe
    except Exception:
        return None
