import requests
from daily_bites_app.errors import BadArgumentError
import os
from dotenv import load_dotenv

load_dotenv()

SPOONACULAR = 'https://api.spoonacular.com/recipes/'

# API Endpoint - /random
def random_recipe(number):
    api_route = 'random?number=' + number + '&apiKey=' + os.environ.get('SPOONACULAR_API_KEY')
    r = requests.get(
        SPOONACULAR + api_route,
    )
    return r.json()
