from app import db

ACCOUNT_TABLE = "account"
MEAL_TABLE = "meal" 
NUT_PER_100_GRAM_TABLE = "nut_per_100_gram" 
FOOD_UNIT_TABLE = "food_unit" 
FOOD_TABLE = "food"
MEAL_LOG_TABLE = "meal_log" 
FOOD_DETAIL_TABLE = "food_detail" 
RECIPE_TABLE = "recipe" 
SAVED_RECIPE_TABLE = "saved_recipe" 
USER_SESSION_TABLE = "user_session"

class Account(db.Model):
    __tablename__ = ACCOUNT_TABLE

    id = db.Column(db.Text, primary_key = True)
    date= db.Column(db.Date, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    # fbid = db.Column(db.Text)
    # diets = db.Column(db.Text)
    # dietary_restrictions = db.Column(db.Text)
    # cuisine_preferences = db.Column(db.Text)

    def __init__(self, id, date, name, email, fbid, diets, dietary_restrictions, cuisine_preferences):
      self.id = id
      self.date = date
      self.name = name
      self.email = email
      # self.fbid = fbid
      # self.diets = diets
      # self.dietary_restrictions = dietary_restrictions
      # self.cuisine_preferences = cuisine_preferences

    def __repr__(self):
        return '<account_id {0}, name {1}>'.format(self.id, self.name)
    