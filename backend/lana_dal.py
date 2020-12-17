import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, ForeignKey, Sequence, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, func, insert
from sqlalchemy.orm import sessionmaker, relationship
from app import db

from datetime import datetime


metadata = MetaData(db)
meal_table = Table('meal', metadata, autoload=True)
food_table = Table('food', metadata, autoload=True)
account_table = Table('account', metadata, autoload=True)
nut_per_100_gram_table = Table('nut_per_100_gram', metadata, autoload=True)
food_unit_table = Table('food_unit', metadata, autoload=True)

# def insert_new_account(id, date_created, name, email): 
#     with db.connect() as connection:
#         i = insert(account_table)
#         statement = i.values({"id": id, "date_created": date_created, "name": name, "email": email})
#         result_set = connection.execute(statement)
#         return result_set

# # Helper Function to check if account_id is in use
# def check_account_id(account_id):
#     with db.connect() as connection:
#         result_set = connection.execute(f"""
#             SELECT count(*) FROM account WHERE id = '{account_id}';
#         """)
#         return result_set.fetchall()[0]


ORM_Base = declarative_base()

class Account(ORM_Base):
    __tablename__ = 'account'
    id = Column(String, primary_key = True )
    date_created = Column(Date)
    name = Column(String)
    email = Column(String)

class Meal(ORM_Base):
    __tablename__ = 'meal'
    meal_id = Column(Integer, primary_key=True)
    account_id = Column(String, ForeignKey('account.id'))
    date_logged = Column(Date)
    category = Column(String)
    account = relationship('Account')

class Nutrition(ORM_Base):
    __tablename__ = 'nut_per_100_gram'
    food_id = Column(String, primary_key=True)
    kcal = Column(Float) 
    protein_g = Column(Float) 
    total_fat_g = Column(Float) 
    total_carb_g = Column(Float) 

class FoodUnit(ORM_Base):
    __tablename__ = 'food_unit'
    food_id = Column(String, primary_key=True)
    unit_desc  = Column(String, primary_key=True)
    grams_per_unit = Column(Float)

class Food(ORM_Base): 
    __tablename__ = 'food'
    meal_id = Column(Integer, primary_key=True)
    food_id = Column(String, primary_key=True)
    food_unit = Column(String)
    food_quantity = Column(String)

Session = sessionmaker(bind=db)
current_session = Session()

def get_daily_nut(user, day): 
    query = current_session.query(Meal).\
        filter(user == Meal.account_id, Meal.date_logged == day)

    return query.all()

def get_food_items(meal_id):
  
    with db.connect() as connection:
        result_set = connection.execute(f"""
            SELECT
                food.food_id,
                food_quantity,
                grams_per_unit,
                kcal,
                protein_g,
                total_fat_g,
                total_carb_g
            FROM
                food
                INNER JOIN food_unit ON food.food_id = food_unit.food_id
                    AND food.food_unit = food_unit.unit_desc
                INNER JOIN nut_per_100_gram ON food.food_id = nut_per_100_gram.food_id
            WHERE
                meal_id = '{meal_id}'
        """)
        result = result_set.fetchall()
        return list(result)