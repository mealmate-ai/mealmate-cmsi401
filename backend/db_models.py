import uuid
from sqlalchemy import Column, Integer, String, Date, ForeignKey
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


def uuid_gen():
    return str(uuid.uuid4())


class Account(Base):
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
    __tablename__ = MEAL_TABLE

    id = Column(String, primary_key=True, default=uuid_gen())
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
