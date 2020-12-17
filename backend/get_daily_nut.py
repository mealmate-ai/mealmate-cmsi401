import sys

from lana_dal import get_daily_nut, get_food_items

# if len(sys.argv) != 3:
#     print('Usage: get_daily_nut <account_id> <date_logged>')
#     exit(1)

# account_id = sys.argv[1]
# date_logged = sys.argv[2]

def calc_nut(account_id, date_logged):
    food_items = []
    total_cal = 0
    total_prot = 0
    total_fat = 0
    total_carb = 0

    try:
        result = get_daily_nut(account_id, date_logged)

        if len(result) == 0:
            return '<User {0} did not log meals on {1}'.format(account_id, date_logged)
   

        for meal in result:
            try:
                food_items += get_food_items(meal.meal_id)
            except ValueError:
                return 'Sorry, something went wrong. Please ensure that {0} is a valid account ID.'.format(account_id)

        for food_item in food_items:
            mult = food_item[2] / 100.0
            total_cal += mult * food_item[3]
            total_prot += mult * food_item[4]
            total_fat += mult * food_item[5]
            total_carb += mult * food_item[6]

        return "FOOD ITEM", total_cal, total_prot, total_fat, total_carb
  
    except ValueError:
        return 'Sorry, something went wrong. Please ensure that {0} is a valid account ID.'.format(account_id)