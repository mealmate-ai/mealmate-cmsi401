from services import dal
from checks import SavedRecipeChecker
from datetime import datetime
import uuid
from dals.models import Recipe, SavedRecipe

from apis.spoonacular import spoonacular


def get_random_recipes(number):
    recipes = spoonacular.random_recipes(number)
    return {'recipes': spoonacular.random_recipes(number)}, 201


def get_recipe_ingredients(recipe_id):
    return {'ingredients': spoonacular.recipe_ingredients(recipe_id)['ingredients']}, 201


def get_recipe_instructions(recipe_id):
    return {'instructions': spoonacular.recipe_instructions(recipe_id)}, 201


def get_recipe_nutrition(recipe_id):
    return {'nutrition': spoonacular.recipe_nutrition(recipe_id)}, 201


def save_recipe(account_id, recipe):
    # first check if recipe is in db
    db_recipe = Recipe.get_recipe_by_id(recipe['id'])

    saved_recipe = {}
    if not db_recipe:
        # add recipe to db if missing
        db_recipe = dal.insert_spoonacular_recipe(recipe)

    saved_recipe['account_id'] = account_id
    saved_recipe['recipe_id'] = recipe['id']
    saved_recipe["date_saved"] = datetime.today().strftime("%Y-%m-%d")

    return {'saved_recipe': dal.insert_saved_recipe(saved_recipe)}, 201