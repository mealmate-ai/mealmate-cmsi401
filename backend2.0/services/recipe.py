from services import dal
from checks import SavedRecipeChecker
from datetime import datetime
import uuid
from dals.models import Recipe, SavedRecipe, Account

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


def save_recipe(account_id, recipe_id):
    # first check if recipe is in db
    db_recipe = Recipe.get_recipe_by_id(recipe_id)

    saved_recipe = {}
    if not db_recipe:
        db_recipe = dal.insert_spoonacular_recipe(recipe_id)

    saved_recipe['account_id'] = account_id
    saved_recipe['recipe_id'] = recipe_id
    saved_recipe["date_saved"] = datetime.today().strftime("%Y-%m-%d")

    return {'saved_recipe': dal.insert_saved_recipe(saved_recipe)}, 201


def get_filtered_recipes(account_id, number):
    import json

    user = dal.get_account_by_id(account_id)

    preferences = {
        'diet': user['diets'] if not None else '',
        'intolerances': user['dietary_restrictions'] if not None else '',
        'cuisine': user['cuisine_preferences'] if not None else '',
    }

    recipes = [
        {
            'id': res['id'],
            'title': res['title'],
            'image': res['image'] if res['image'] else '',
            'cuisine': ' '.join(res['cuisines']),
            'liked': False,
            'instructions': res['instructions'],
            'ingredients': [
                ' '.join(
                    [
                        str(ing['measures']['us']['amount']),
                        ing['measures']['us']['unitShort'],
                        ing['name'],
                    ]
                )
                for ing in res['extendedIngredients']
            ],
        }
        for res in spoonacular.get_tailored_recipes(preferences, number)
    ]

    return {'recipes': recipes}, 201


def recipes_list(account_id):
    return {'saved_recipes': dal.get_recipes_list(account_id)}, 200


def bulk_recipe_lookup(account_id):
    return {'recipes': dal.spoonacular_recipes_list(account_id)}, 200


def recipe_details(recipe_id):
    response = dal.get_recipe_details(recipe_id)
    print(response, type(response), response is None)
    if response is None:
        return {'error': "Error occured when attempting to call Spoonacular API"}, 400
    return {'recipe': response}, 200