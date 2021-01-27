import requests
from daily_bites_app.errors import BadArgumentError
import os
from dotenv import load_dotenv

load_dotenv()

SPOONACULAR = 'https://api.spoonacular.com/recipes/'

# API Endpoint - /random
def random_recipes(number):
    api_route = 'random?number=' + str(number) + '&apiKey=' + os.environ.get('SPOONACULAR_API_KEY')
    r = requests.get(
        SPOONACULAR + api_route,
    )
    return r.json()


def recipe_nutrition(recipe_id):
    api_route = (
        str(recipe_id)
        + '/nutritionWidget.json'
        + '?apiKey='
        + os.environ.get('SPOONACULAR_API_KEY')
    )
    r = requests.get(
        SPOONACULAR + api_route,
    )
    return r.json()


def recipe_ingredients(recipe_id):
    api_route = (
        str(recipe_id)
        + '/ingredientWidget.json'
        + '?apiKey='
        + os.environ.get('SPOONACULAR_API_KEY')
    )
    r = requests.get(
        SPOONACULAR + api_route,
    )

    return r.json()


def recipe_instructions(recipe_id):
    api_route = (
        str(recipe_id)
        + '/analyzedInstructions'
        + '?apiKey='
        + os.environ.get('SPOONACULAR_API_KEY')
    )
    r = requests.get(
        SPOONACULAR + api_route,
    )

    return r.json()