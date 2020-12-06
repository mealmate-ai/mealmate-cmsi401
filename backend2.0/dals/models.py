from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence
from sqlalchemy.sql import func, or_
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR, UUID

from daily_bites_app.errors import BadArgumentError

from daily_bites_app.routes import app
import uuid

db = SQLAlchemy(app)

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


class ReturnHelper:
    def value_for(self, key):
        return getattr(self, key)

    def as_dict(self, fields):
        keys = [key for key in getattr(type(self), fields)]
        return {key: self.value_for(key) for key in keys}

    def min_view(self):
        return self.as_dict("min_fields")

    def search_result_view(self):
        return self.as_dict("search_result_fields")

    def full_view(self):
        return self.as_dict("all_fields")


class Account(db.Model, ReturnHelper):
    """
    Daily Bites account table - store users of application
    """

    __tablename__ = ACCOUNT_TABLE

    id = db.Column(db.String(36), primary_key=True)
    date_created = db.Column(db.Date)
    name = db.Column(db.String(128))
    email = db.Column(db.String(256))
    diets = db.Column(db.Text)
    dietary_restrictions = db.Column(db.Text)
    cuisine_preferences = db.Column(db.Text)
    fbid = db.Column(db.String(128))

    min_fields = {"id"}
    search_result_fields = {*min_fields, "name", "email", "date_created"}
    all_fields = {*search_result_fields, "diets", "dietary_restrictions", "cuisine_preferences"}

    @classmethod
    def get_account_by_id(cls, id):
        """
        find account details using account id
        """
        return cls.query.filter_by(id=id).first()


class Meal(db.Model, ReturnHelper):
    """
    Daily Bites meal table - record meals that users log
    """

    __tablename__ = MEAL_TABLE

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = db.Column(db.String(36), db.ForeignKey("account.id"))
    date_logged = db.Column(db.Date)
    category = db.Column(db.String(15))

    min_fields = {"id", "account_id"}
    search_result_fields = {*min_fields, "date_logged"}
    all_fields = {*search_result_fields, "category"}

    @classmethod
    def get_meal_by_id(cls, meal_id):
        meal = cls.query.filter_by(id=meal_id).first()
        # do a check here for meal
        if meal is None:
            raise BadArgumentError("No such meal")
        return meal


class Nutrition(db.Model, ReturnHelper):
    """
    Daily Bites nut_per_100_gram table - look up table for food nutrition
    """

    __tablename__ = NUT_PER_100_GRAM_TABLE
    food_id = db.Column(db.String(36), primary_key=True)
    kcal = db.Column(db.Float)
    protein_g = db.Column(db.Float)
    total_fat_g = db.Column(db.Float)
    total_carb_g = db.Column(db.Float)
    total_diet_fiber_g = db.Column(db.Float)
    calcium_mg = db.Column(db.Float)
    iron_mg = db.Column(db.Float)
    magnesium_mg = db.Column(db.Float)
    phosphorus_mg = db.Column(db.Float)
    potassium_mg = db.Column(db.Float)
    sodium_mg = db.Column(db.Float)
    zinc_mg = db.Column(db.Float)
    copper_mg = db.Column(db.Float)
    manganese_mg = db.Column(db.Float)
    selenium_mcg = db.Column(db.Float)
    vitamin_c_mg = db.Column(db.Float)
    thiamin_mg = db.Column(db.Float)
    riboflavin_mg = db.Column(db.Float)
    niacin_mg = db.Column(db.Float)
    pantothenic_acid_mg = db.Column(db.Float)
    vitamin_b6_mg = db.Column(db.Float)
    total_folate_mcg = db.Column(db.Float)
    vitamin_b12_mcg = db.Column(db.Float)
    vitamin_d_mcg = db.Column(db.Float)
    vitamin_e_mg = db.Column(db.Float)
    vitamin_k_mcg = db.Column(db.Float)
    total_sat_fat_g = db.Column(db.Float)
    total_monounsat_fat_g = db.Column(db.Float)
    total_poly_unsat_fat_g = db.Column(db.Float)
    total_trans_fat_g = db.Column(db.Float)
    cholesterol_mg = db.Column(db.Float)
    total_sugar_g = db.Column(db.Float)
    omega_3_fatty_acids_g = db.Column(db.Float)

    min_fields = {"food_id"}
    search_result_fields = {*min_fields, "kcal", "protein_g", "total_fat_g", "total_carb_g"}
    all_fields = {
        *search_result_fields,
        "total_carb_g",
        "total_diet_fiber_g",
        "calcium_mg",
        "iron_mg",
        "magnesium_mg",
        "phosphorus_mg",
        "potassium_mg",
        "sodium_mg",
        "zinc_mg",
        "copper_mg",
        "manganese_mg",
        "selenium_mcg",
        "vitamin_c_mg",
        "thiamin_mg",
        "riboflavin_mg",
        "niacin_mg",
        "pantothenic_acid_mg",
        "vitamin_b6_mg",
        "total_folate_mcg",
        "vitamin_b12_mcg",
        "vitamin_d_mcg",
        "vitamin_e_mg",
        "vitamin_k_mcg",
        "total_sat_fat_g",
        "total_monounsat_fat_g",
        "total_poly_unsat_fat_g",
        "total_trans_fat_g",
        "cholesterol_mg",
        "total_sugar_g",
        "omega_3_fatty_acids_g",
    }

    @classmethod
    def get_food_by_id(cls, food_id):
        food = cls.query.filter_by(food_id=food_id).first()
        # do a check if missing food - means there has been an error
        return food


class FoodUnit(db.Model, ReturnHelper):
    """
    Daily Bites food_unit table - look up table for food unit conversions
    """

    __tablename__ = FOOD_UNIT_TABLE

    food_id = db.Column(db.String(36), db.ForeignKey("nut_per_100_gram.food_id"), primary_key=True)
    unit_desc = db.Column(db.String(256), primary_key=True)
    grams_per_unit = db.Column(db.Float)

    min_fields = {"food_id", "unit_desc"}
    search_result_fields = {*min_fields, "grams_per_unit"}
    all_fields = {*search_result_fields}

    @classmethod
    def get_all_units_by_id(cls, food_id):
        return cls.query.filter_by(food_id=food_id).all()

    @classmethod
    def get_unit_by_id_and_desc(cls, food_id, desc):
        return cls.query.filter_by(food_id=food_id, unit_desc=desc).first()


class Food(db.Model, ReturnHelper):
    """
    Daily Bites food table - records the food item and quantity for a food logged
    """

    __tablename__ = FOOD_TABLE

    meal_id = db.Column(UUID(as_uuid=True), db.ForeignKey("meal.id"), primary_key=True)
    food_id = db.Column(db.String(36), db.ForeignKey("nut_per_100_gram.food_id"), primary_key=True)
    log_id = db.Column(db.Integer)  # could probably get rid of this
    food_unit = db.Column(db.String(256))
    food_quantity = db.Column(db.String(256))

    min_fields = {"food_id", "meal_id"}
    search_result_fields = {*min_fields, "log_id"}
    all_fields = {*search_result_fields, "food_unit", "food_quantity"}

    @classmethod
    def get_foods_by_meal_id(cls, meal_id):
        return cls.query.filter_by(meal_id=meal_id).all()

    @classmethod
    def get_food_by_id(cls, food_id):
        return cls.query.filter_by(meal_id=meal_id).all()


class MealLog(db.Model, ReturnHelper):
    """
    Daily Bites meal_log table - records the raw text for a meal logged
    """

    __tablename__ = MEAL_LOG_TABLE

    log_seq = Sequence("log_id_seq")
    meal_id = db.Column(UUID(as_uuid=True), db.ForeignKey("meal.id"), primary_key=True)
    log_id = db.Column(db.Integer, log_seq, primary_key=True, server_default=log_seq.next_value())
    raw_text = db.Column(db.Text)

    min_fields = {"meal_id"}
    search_result_fields = {*min_fields, "log_id"}
    all_fields = {*search_result_fields, "raw_text"}


class FoodDetail(db.Model, ReturnHelper):
    """
    Daily Bites food_detail table - provides details for food recorded
    """

    __tablename__ = FOOD_DETAIL_TABLE

    food_id = db.Column(db.String(36), db.ForeignKey("nut_per_100_gram.food_id"), primary_key=True)
    food_desc = db.Column(db.String(256))
    barcode = db.Column(db.String(50))
    brand = db.Column(db.String(256))

    __table_args__ = (
        db.Index(
            "ix_food_detail_food_desc",
            func.to_tsvector("english", food_desc),
            postgresql_using="gin",
        ),
    )

    min_fields = {"food_id"}
    search_result_fields = {*min_fields, "barcode", "brand"}
    all_fields = {*search_result_fields, "food_desc"}

    @classmethod
    def get_food_detail_by_id(cls, food_id):
        return cls.query.filter_by(food_id=food_id).first()


class Recipe(db.Model, ReturnHelper):
    """
    Daily Bites recipe table - stores recipes that recommend to user from Spoonacular
    """

    __tablename__ = RECIPE_TABLE

    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    recipe_desc = db.Column(db.Text)
    recipe_ingredients = db.Column(db.Text)
    recipe_instructions = db.Column(db.Text)

    min_fields = {"recipe_id"}
    search_result_fields = {*min_fields, "title"}
    all_fields = {*search_result_fields, "recipe_desc", "recipe_instructions", "recipe_ingredients"}

    @classmethod
    def get_recipe_by_id(cls, recipe_id):
        return cls.query.filter_by(recipe_id=recipe_id).all()


class SavedRecipe(db.Model, ReturnHelper):
    """
    Daily Bites saved_recipe table - records saved recipes for user
    """

    __tablename__ = SAVED_RECIPE_TABLE

    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.recipe_id"), primary_key=True)
    account_id = db.Column(db.String(36), db.ForeignKey("account.id"), primary_key=True)
    date_saved = db.Column(db.Date)

    min_fields = {"recipe_id"}
    search_result_fields = {*min_fields, "account_id"}
    all_fields = {*search_result_fields, "date_saved"}

    @classmethod
    def get_saved_recipes_by_user(cls, account_id):
        return cls.query.filter_by(account_id=account_id).all()


class UserSession(db.Model, ReturnHelper):
    """
    Daily Bites user_session table - records user's interaction with the app
    """

    __tablename__ = USER_SESSION_TABLE

    session_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    account_id = db.Column(db.String(36), db.ForeignKey("account.id"))
    date = db.Column(db.Date)
    time_started = db.Column(db.DateTime)
    time_completed = db.Column(db.DateTime)
    num_clicks = db.Column(db.Integer)
    screens_visited = db.Column(db.Date)
    logged_meal = db.Column(db.Boolean)

    min_fields = {"session_id", "account_id"}
    search_result_fields = {*min_fields, "date"}
    all_fields = {
        *search_result_fields,
        "time_started",
        "time_completed",
        "num_clicks",
        "screens_visited",
        "logged_meal",
    }

    @classmethod
    def get_session_by_id(cls, session_id):
        return cls.query.filter_by(session_id=session_id).all()
