"""
https://github.com/mkorpusik/mealmate/blob/35dff82faa3e5c3cbdeb269e69a1cdca1b8b38bb/flask_server/nutritionix.py
"""

import requests
import load_nut_map
from daily_bites_app.errors import BadArgumentError
import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX = 'https://trackapi.nutritionix.com/v2/'
NUT_MAP = load_nut_map.load_nut_map()


def barcode_to_food(barcode):
    api_route = 'search/item?upc=' + str(barcode)
    r = requests.get(
        NUTRITIONIX + api_route,
        headers={
            'x-app-id': str(os.environ.get('NUTRITIONIX_APP_ID')),
            'x-app-key': str(os.environ.get('NUTRITIONIX_API_KEY')),
        },
    )
    return server_format(r.json(), barcode)


def get_food_units(res):
    units = [(res['serving_unit'], res['grams_per_unit'])]
    # Add serving quantity to unit_desc.
    if 'serving_qty' in res and float(res['serving_qty']) != 1.0:
        units = [
            (
                'serving (' + str(res['serving_qty']) + ' ' + res['serving_unit'] + ')',
                res['grams_per_unit'],
            )
        ]
        # Add another unit that's normalized to have quantity 1.
        unit_desc = res['serving_unit']
        grams_per_unit = res['grams_per_unit'] / float(res['serving_qty'])
        units.append((unit_desc, grams_per_unit))
    units = add_missing_units(units, res)
    units_arr = [{'unit_desc': unit[0], 'grams_per_unit': unit[1]} for unit in units]

    return units_arr


def server_format(payload, upc):
    '''Converts Nutritionix API results to db mapping format.'''

    new_food = {}
    if 'foods' not in payload:
        raise BadArgumentError('invalid barcode provided')

    food = payload['foods'][0]
    div = food['serving_weight_grams'] if food['serving_weight_grams'] else 100.0

    scale = 100.0 / div

    unit_res = {
        'serving_qty': food['serving_qty'],
        'serving_unit': food['serving_unit'],
        'grams_per_unit': food['serving_weight_grams'] if food['serving_weight_grams'] else 100.0,
    }

    brand = food['brand_name'] if 'brand_name' in food else ''
    new_food['food_detail'] = {
        'food_desc': food['food_name'] + ', ' + brand if len(brand) > 0 else food['food_name'],
        'barcode': upc,
        'brand': brand,
    }
    new_food['image'] = food['photo']['thumb']
    new_food['nutrition'] = convert_to_nut_map(food['full_nutrients'], scale)
    new_food['food_units'] = get_food_units(unit_res)

    return new_food


def scaled_if_present(value, factor):
    '''Optional scaling of nutrient value.'''
    if value is not None:
        return factor * value


def convert_to_nut_map(nutrients, scale):
    '''Converts Nutritionix nutrients to USDA naming convention.'''
    nut_map = {}
    for nut in nutrients:
        attr_id = str(nut['attr_id'])
        nut_obj = NUT_MAP[attr_id]
        nut_map[nut_obj.name] = scaled_if_present(nut['value'], scale)
    return nut_map


def add_missing_units(units, res):
    '''For any missing units, use default values for grams per unit.'''
    grams_per_unit = res['grams_per_unit'] / float(res['serving_qty'])
    if 'tsp' in res['serving_unit']:
        units.append(('cup', grams_per_unit * 48.0))
        units.append(('tbsp', grams_per_unit * 3.0))
    if 'tbsp' in res['serving_unit']:
        units.append(('cup', grams_per_unit * 16.0))
        units.append(('tsp', grams_per_unit / 3.0))
    if 'cup' in res['serving_unit']:
        units.append(('tsp', grams_per_unit / 48.0))
        units.append(('tbsp', grams_per_unit / 16.0))
    if 'ml' == res['serving_unit']:
        units.append(('oz', grams_per_unit * 29.5735))
        units.append(('cup', grams_per_unit * 29.5735 * 8))
        units.append(('tbsp', grams_per_unit * 29.5735 / 2))
        units.append(('tsp', grams_per_unit * 29.5735 / 6))
    return units