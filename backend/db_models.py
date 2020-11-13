from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

class Account(Base):
    __tablename__ = ACCOUNT_TABLE

    id = Column(String, primary_key = True)
    date_created = Column(Date, primary_key = True)
    name = Column(String)
    email = Column(String)

    def __init__(self, id, date_created, name, email):
      self.id = id
      self.date_created = date_created
      self.name = name
      self.email = email

    def __repr__(self):
        return '<account_id {0}, name {1}>'.format(self.id, self.name)
    