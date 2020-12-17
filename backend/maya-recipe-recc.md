# Recipe Reccomendations 

Todo next semester: 
- Hook the code up to the database in RDS
- Integrate the code into the Front-End 

### app.py

```
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

'''
Route to get a list of nutrients in a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

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

'''
Route to get a list of ingredients for a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

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

'''
Route to get instructions of a recipe from Spoonacular
    - Requires in recipe_id and user_id
'''

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


'''
Route to get a users saved recipes
    - Requires in user_id
'''
@app.route("/savedrecipes/<int:recipe_id>", methods=["GET"]) 
def get_saved_recipes(user_id):
    

if __name__ == '__main__':
    # To create/use the database mentioned in the URI, run the create_all() method.
    # db.create_all()
    app.run()
```

### requirements.txt

```
aniso8601==8.0.0
click==7.1.2
Flask==1.1.2
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pytz==2020.1
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==1.0.1
requests==2.25.0
```
