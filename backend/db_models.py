import uuid
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Float,
    Boolean,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

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
    """
    Daily Bites account table - store users of application
    """

    __tablename__ = ACCOUNT_TABLE

    id = Column(String, primary_key=True)
    date_created = Column(Date)
    name = Column(String)
    email = Column(String)
    diets = Column(String)
    dietary_restrictions = Column(String)
    cuisine_preferences = Column(String)
    fbid = Column(String)

    def __init__(
        self,
        id,
        date_created,
        name,
        email,
        diets,
        dietary_restrictions,
        cuisine_preferences,
        fbid,
    ):
        self.id = id
        self.date_created = date_created
        self.name = name
        self.email = email
        self.diets = diets
        self.dietary_restrictions = dietary_restrictions
        self.cuisine_preferences = cuisine_preferences
        self.fbid = fbid

    def __repr__(self):
        return "<account_id {0}, name {1}>".format(self.id, self.name)


class Meal(Base):
    """
    Daily Bites meal table - record meals that users log
    """

    __tablename__ = MEAL_TABLE

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = Column(String, ForeignKey("account.id"))
    date_logged = Column(Date)
    category = Column(String)

    def __init__(self, id, account_id, date_logged, category):
        self.id = id
        self.account_id = account_id
        self.date_logged = date_logged
        self.category = category

    def __repr__(self):
        return "<meal_id {0}, account_id {1}>".format(self.id, self.account_id)


class Nutrition(Base):
    """
    Daily Bites nut_per_100_gram table - look up table for food nutrition
    """

    __tablename__ = NUT_PER_100_GRAM_TABLE
    food_id = Column(String, primary_key=True)
    kcal = Column(Float)
    protein_g = Column(Float)
    total_fat_g = Column(Float)
    total_carb_g = Column(Float)

    # need to add more nuts
    def __init__(self, food_id, kcal, protein_g, total_fat_g, total_carb_g):
        self.food_id = food_id
        self.kcal = kcal
        self.protein_g = protein_g
        self.total_fat_g = total_fat_g
        self.total_carb_g = total_carb_g

    def __repr__(self):
        return "<food_id {0}, kcal {1}>".format(self.food_id, self.kcal)


class FoodUnit(Base):
    """
    Daily Bites food_unit table - look up table for food unit conversions
    """

    __tablename__ = FOOD_UNIT_TABLE

    food_id = Column(String, ForeignKey("account.id"), primary_key=True)
    unit_desc = Column(String, primary_key=True)
    grams_per_unit = Column(Float)

    def __init__(self, food_id, unit_desc, grams_per_unit):
        self.food_id = food_id
        self.unit_desc = unit_desc
        self.grams_per_unit = grams_per_unit

    def __repr__(self):
        return "<food_id {0}, unit {1}>".format(self.food_id, self.unit_desc)


class Food(Base):
    """
    Daily Bites food table - records the food item and quantity for a food logged
    """

    __tablename__ = FOOD_TABLE

    meal_id = Column(UUID(as_uuid=True), ForeignKey("meal.id"), primary_key=True)
    food_id = Column(String, ForeignKey("nut_per_100_gram.id"), primary_key=True)
    log_id = Column(Integer)
    food_desc = Column(String)
    food_unit = Column(String)
    food_quantity = Column(String)

    def __init__(self, meal_id, food_id, log_id, food_desc, food_unit, food_quantity):
        self.meal_id = meal_id
        self.food_id = food_id
        self.log_id = log_id
        self.food_desc = food_desc
        self.food_unit = food_unit
        self.food_quantity = food_quantity

    def __repr__(self):
        return "<meal_id {0}, food_id {1}>".format(self.meal_id, self.food_id)


class MealLog(Base):
    """
    Daily Bites meal_log table - records the raw text for a meal logged
    """

    __tablename__ = MEAL_LOG_TABLE

    meal_id = Column(UUID(as_uuid=True), ForeignKey("meal.id"), primary_key=True)
    log_id = Column(Integer, primary_key=True)
    raw_text = Column(String)

    def __init__(self, meal_id, log_id, raw_text):
        self.meal_id = meal_id
        self.log_id = log_id
        self.raw_text = raw_text

    def __repr__(self):
        return "<meal_id {0}, raw_text {1}>".format(self.meal_id, self.raw_text)


class FoodDetail(Base):
    """
    Daily Bites food_detail table - provides details for food recorded
    """

    __tablename__ = FOOD_DETAIL_TABLE

    food_id = Column(String, ForeignKey("nut_per_100_gram.id"), primary_key=True)
    food_desc = Column(String)
    barcode = Column(String)
    brand = Column(String)
    food_group = Column(String)
    ingredient_list = Column(String)

    def __init__(self, food_id, food_desc, barcode, brand, food_group, ingredient_list):
        self.food_id = food_id
        self.food_desc = food_desc
        self.barcode = barcode
        self.brand = brand
        self.food_group = food_group
        self.ingredient_list = ingredient_list

    def __repr__(self):
        return "<food_id {0}, desc {1}>".format(self.food_id, self.food_desc)


class Recipe(Base):
    """
    Daily Bites recipe table - stores recipes that recommend to user from Spoonacular
    """

    __tablename__ = RECIPE_TABLE

    recipe_id = Column(Integer, primary_key=True)
    title = Column(String)
    recipe_desc = Column(String)
    recipe_ingredients = Column(String)
    recipe_instructions = Column(String)

    def __init__(
        self, recipe_id, title, recipe_desc, recipe_ingredients, recipe_instructions
    ):
        self.recipe_id = recipe_id
        self.title = title
        self.recipe_desc = recipe_desc
        self.recipe_ingredients = recipe_ingredients
        self.recipe_instructions = recipe_instructions

    def __repr__(self):
        return "<food_id {0}, title {1}>".format(self.recipe_id, self.title)


class SavedRecipe(Base):
    """
    Daily Bites saved_recipe table - records saved recipes for user
    """

    __tablename__ = SAVED_RECIPE_TABLE

    recipe_id = Column(Integer, ForeignKey("recipe.id"), primary_key=True)
    account_id = Column(String, ForeignKey("account.id"), primary_key=True)
    date_saved = Column(Date)

    def __init__(self, recipe_id, account_id, date_saved):
        self.recipe_id = recipe_id
        self.account_id = account_id
        self.date_saved = date_saved

    def __repr__(self):
        return "<meal_id {0}, account_id {1}>".format(self.recipe_id, self.account_id)


class UserSession(Base):
    """
    Daily Bites user_session table - records user's interaction with the app
    """

    __tablename__ = USER_SESSION_TABLE

    session_id = Column(String, primary_key=True)
    account_id = Column(String, ForeignKey("account.id"))
    date = Column(Date)
    time_started = Column(DateTime)
    time_completed = Column(DateTime)
    num_clicks = Column(Integer)
    screens_visited = Column(Date)
    logged_meal = Column(Boolean)

    def __init__(
        self,
        session_id,
        account_id,
        date,
        time_started,
        time_completed,
        num_clicks,
        screens_visited,
        logged_meal,
    ):
        self.session_id = session_id
        self.account_id = account_id
        self.date = date
        self.time_started = time_started
        self.time_completed = time_completed
        self.num_clicks = num_clicks
        self.screens_visited = screens_visited
        self.logged_meal = logged_meal

    def __repr__(self):
        return "<session_id {0}, account_id {1}>".format(
            self.session_id, self.account_id
        )
