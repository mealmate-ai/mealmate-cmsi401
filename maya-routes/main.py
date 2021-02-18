from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import random 

app = Flask(__name__)
app.config["DEBUG"] = True

api_key = '954290f038ba44a7b0c7b1ddc2ce0714'

'''
Route to get a list at most 5 recipes from Spoonacular
    - Requires in user_id
'''

@app.route("/recipes/<user_id>", methods=["GET"])
def get_recipes(user_id):

    # Test info -----------------------------------------------------
    list_of_cuisines = ['African','American','British','Cajun','Caribbean',
    'Chinese','Eastern European','European','French','German','Greek','Indian',
    'Irish','Italian','Japanese','Jewish','Korean','Latin American','Mediterranean',
    'Mexican','Middle Eastern','Nordic','Southern','Spanish','Thai','Vietnamese']
    list_of_diets = ['Gluten Free','Ketogenic','Vegetarian','Lacto-Vegetarian',
    'Ovo-Vegetarian','Vegan','Pescatarian','Paleo','Primal','Whole30','None']
    list_of_intolerances = ['Dairy','Egg','Gluten','Grain','Peanut','Seafood','Sesame',
    'Shellfish','Soy','Sulfite','Tree Nut','Wheat','None']
    # -----------------------------------------------------
    
    # 1.  get quiz information from db 
            # Note: If no options are checkmarked in the quiz for a specific question that means 'None'
    # 1a. if existing user, get history of meals from db (a few of users last eaten meals) 
    # 2.  if there are any, get liked recipes from db (for later use in 4.)
    # 3.  form query for spoonacular using history meals and quiz info to get 10 meals 
            # Note: You may have to query multiple times to get more recipes, change query/cuisine to get more results
    # 3a. in the api put in:
            # query (can be specific food items based on history of meals (1a.))
                # ex: pasta, peanut butter, chicken
            # cuisine (based on quiz)
            # diet (based on quiz)
            # intolerances (based on quiz)
    # 4.  remove liked recipes 
    # 5.  return up to 5 recipes

    # -----------------------------------------------------

    # if new user:
        # query = 'None'
    # else (if old user):
        # query is one random food based on users history

    # for now make query None
    query = 'None'

    # get the users choice of cuisine
    cuisine = random.choice(list_of_cuisines)

    # get the users diet
    diet = random.choice(list_of_diets) 

    # get the user intolerances(s)
    some_intolerances = random.sample(list_of_intolerances, 2)
    intolerances = ''
    for i in some_intolerances:
        if i == 'None':
            intolerances = 'None'
            break
    intolerances = ','.join(some_intolerances)
    
    payload = {'query': query, 'cuisine': cuisine, 'diet': diet, 'intolerances': intolerances, 'apiKey': api_key}
    response = requests.get('https://api.spoonacular.com/recipes/complexSearch', params = payload)
    # print('URL: ', response.url)
    # print('ENCODING: ', response.encoding)
    # print('STATUS_CODE: ', response.status_code)
    # print('HEADERS: ', response.headers)
    # print('TEXT: ', response.text)
    # print('CONTENT: ', response.content)
    # print('JSON: ', response.json)

    if response.status_code == 200:
        data = response.json() 
        totalResults = str(data['totalResults'])
        recipes = []
        for i in range(int(totalResults)):
            if len(recipes) < 5:
                dict_copy = data['results'][i].copy()
                recipes.append(dict_copy) 
            else: 
                break
    else: 
        return f'Sorry, there was an {response.status_code} error. Please try again.'
    return {'recipes': f'{recipes}'}

'''
Route to get a list of nutrients in a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

@app.route('/nutrients/<recipe_id>/<user_id>', methods=['GET'])
def get_nutrients(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json', params = payload)
    # print('URL: ', response.url)
    # print('ENCODING: ', response.encoding)
    # print('STATUS_CODE: ', response.status_code)
    # print('HEADERS: ', response.headers)
    # print('TEXT: ', response.text)
    # print('CONTENT: ', response.content)
    # print('JSON: ', response.json)

    if response.status_code == 200:
        nutrients = response.json()
    else:
        return f'Sorry, there was an {response.status_code} error. Please try again.'
    return nutrients

'''
Route to get a list of ingredients for a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

@app.route('/ingredients/<recipe_id>/<user_id>', methods=['GET'])
def get_ingredients(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json', params = payload)
    # print('URL: ', response.url)
    # print('ENCODING: ', response.encoding)
    # print('STATUS_CODE: ', response.status_code)
    # print('HEADERS: ', response.headers)
    # print('TEXT: ', response.text)
    # print('CONTENT: ', response.content)
    # print('JSON: ', response.json)

    if response.status_code == 200:
        data = response.json()
        if not data: 
            return 'Sorry, there are no instructions for this recipe.'
        else:
            result = []
            i = 0
            while i < len(data['ingredients']):
                ingred_info = {'name':'', 'value':'', 'unit': ''}
                curr_ingred = data['ingredients'][i]
                ingred_info['name'] = curr_ingred['name']
                ingred_info['value'] = curr_ingred['amount']['us']['value']
                ingred_info['unit'] = curr_ingred['amount']['us']['unit']
                result.append(ingred_info)
                i += 1
    else:
        return f'Sorry, there was an {response.status_code} error. Please try again.'
    return {'ingredients': f'{result}'}

'''
Route to get instructions of a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

@app.route('/instructions/<recipe_id>/<user_id>', methods=['GET'])
def get_instruction(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions', params = payload)
    # print('URL: ', response.url)
    # print('ENCODING: ', response.encoding)
    # print('STATUS_CODE: ', response.status_code)
    # print('HEADERS: ', response.headers)
    # print('TEXT: ', response.text)
    # print('CONTENT: ', response.content)
    # print('JSON: ', response.json)

    if response.status_code == 200:
        data = response.json()
        if not data:
            return 'Sorry, there are no instructions for this recipe.' 
        else:
            result = []
            i = 0
            while i < len(data[0]['steps']):
                step_info = {'number':'', 'step':''}
                curr_step = data[0]['steps'][i]
                step_info['number'] = curr_step['number']
                step_info['step'] = curr_step['step']
                result.append(step_info)
                i += 1
    else:
        return f'Sorry, there was an {response.status_code} error. Please try again.'
    return {'steps': f'{result}'}


'''
Route to get a users saved recipes
    - Requires in user_id
'''
@app.route("/savedrecipes/<int:recipe_id>", methods=["GET"]) 
def get_saved_recipes(user_id):
    # use the user_id get a list of saved recipes
        # when a recipe is saved, save the recipe_id in the database for easy retreival
    return TODO
    
if __name__ == '__main__':
    # To create/use the database mentioned in the URI, run the create_all() method.
    # db.create_all()
    app.run()