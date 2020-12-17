# Recipe Reccomendations 

Todo next semester: 
- Hook the code up to the database
- Hook the code up to AWS
- Integrate the code into the Front-End 

```
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import random 

# Now create a Flask application object and set URI for the database to be used.
app = Flask(__name__)
app.config["DEBUG"] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'lana-database-copy.czvpopdnxi2n.us-east-2.rds.amazonaws.com'

api_key = '954290f038ba44a7b0c7b1ddc2ce0714'

@app.route("/hello", methods=["GET"])
def hello_world():
    return 'Hello World!'

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

    # 1. use user_id to query quiz from db 
    # 2. use user_id to query liked recipes from db 
    # 3. form query for spoonacular
    # 4. remove recipes already favorite
    # 5. return up to 5

    # if new user:
        # query = 'None'
    # else (if old user):
        # query is one random food based on users history

    # for now make query None
    query = 'None'

    # get the users choice of cuisine
    cuisine = random.choice(list_of_cuisines)

    # get the users diet?
    diet = random.choice(list_of_diets) 

    # get the user intolerances(s)?
    some_intolerances = random.sample(list_of_intolerances, 2)
    intolerances = ''
    for i in some_intolerances:
        if i == 'None':
            intolerances = 'None'
            break
    intolerances = ','.join(some_intolerances)
    #-----------------------------------------------------
    
    payload = {'query': query, 'cuisine': cuisine, 'diet': diet, 'intolerances': intolerances, 'apiKey': api_key}
    response = requests.get('https://api.spoonacular.com/recipes/complexSearch', params = payload)
    print('URL: ', response.url)
    print('ENCODING: ', response.encoding)
    print('STATUS_CODE: ', response.status_code)
    print('HEADERS: ', response.headers)
    print('TEXT: ', response.text)
    print('CONTENT: ', response.content)
    print('JSON: ', response.json)

    #recipe_id = 
    # return ==> results[{id, title, image}, ...]
    # return jsonify({
    #     'id': recipe_id,
    #     'title': title,
    #     'image': image
    # })

    return response.text;

@app.route('/nutrients/<int:recipe_id>/<user_id>', methods=['GET'])
def get_nutrients(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get('https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json', params = payload)
    print('URL: ', response.url)
    print('ENCODING: ', response.encoding)
    print('STATUS_CODE: ', response.status_code)
    print('HEADERS: ', response.headers)
    print('TEXT: ', response.text)
    print('CONTENT: ', response.content)
    print('JSON: ', response.json)

    # return ==> {calories, carbs, fat, protien}
    return jsonify({
        'calories': calories,
        'carbs': carbs,
        'fat': fat,
        'unit': protein
    })

@app.route('/ingredients/<int:recipe_id>/<user_id>', methods=['GET'])
def get_ingredients(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get('https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json', params = payload)
    print('URL: ', response.url)
    print('ENCODING: ', response.encoding)
    print('STATUS_CODE: ', response.status_code)
    print('HEADERS: ', response.headers)
    print('TEXT: ', response.text)
    print('CONTENT: ', response.content)
    print('JSON: ', response.json)

    # return ==> {ingredients[{name, image, amount{ us{ value, unit }}}, ...]}
    return jsonify({
        'name': name,
        'image': image,
        'value': value,
        'unit': unit
    })

@app.route('/instructions/<int:recipe_id>/<user_id>', methods=['GET'])
def get_instruction(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get('https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions', params = payload)
    print('URL: ', response.url)
    print('ENCODING: ', response.encoding)
    print('STATUS_CODE: ', response.status_code)
    print('HEADERS: ', response.headers)
    print('TEXT: ', response.text)
    print('CONTENT: ', response.content)
    print('JSON: ', response.json)

    # return ==> [{steps:[{number, step}, {number, step}, ..., {number, step} ]}]
    return jsonify({
        'number': number,
        'step': step
    })

@app.route("/savedrecipes/<int:recipe_id>", methods=["GET"]) 
def get_saved_recipes(recipe_id, user_id):
    payload = {'apiKey': api_key}
    response = requests.get("https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions", params = payload)
    print('URL: ', response.url)
    print('ENCODING: ', response.encoding)
    print('STATUS_CODE: ', response.status_code)
    print('HEADERS: ', response.headers)
    print('TEXT: ', response.text)
    print('CONTENT: ', response.content)
    print('JSON: ', response.json)

    # return ==> [{steps:[{number, step}, {number, step}, ..., {number, step} ]}]
    return jsonify({
        'number': number,
        'step': step
    })

if __name__ == '__main__':
    # To create/use the database mentioned in the URI, run the create_all() method.
    #db.create_all()
    app.run()
```

