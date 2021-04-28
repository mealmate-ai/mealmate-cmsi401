from services import dal
from checks import MealChecker, MealLogChecker, ChatbotChecker
from datetime import datetime
import uuid
from dals.models import Meal
from dailybitestagger import get_tags
import json


def tag_and_create_meal(account_id, request):
    chatArgs = ChatbotChecker.__on_creation__(request)
    meal = {}
    meal["id"] = uuid.uuid4()
    meal["account_id"] = account_id
    meal["date_logged"] = datetime.today().strftime("%Y-%m-%d")
    meal['category'] = chatArgs['category']
    newMeal = dal.create_meal(meal)
    tags = get_tags(chatArgs['raw_text'])
    for tag in json.loads(tags):
        print(type(tag['Food']))
        matches = dal.search_mv_foods('peanut butter')
        print(matches)

    return {'meal': newMeal}, 200