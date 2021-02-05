from checks.helpers import *
from daily_bites_app.errors import BadArgumentError


def checked(obj, requirements, convert_missing_nut_to_zero=False):
    if not isinstance(obj, dict):
        raise BadArgumentError("Invalid arguments provided, JSON required")
    checkedArgs = {}

    for key, constraint in requirements.items():
        value = obj.get(key)

        for check in constraint:
            check(key, value)
        if value is not None:
            checkedArgs[key] = value

        elif convert_missing_nut_to_zero:
            checkedArgs[key] = 0.0

    return checkedArgs


class Checker:
    @classmethod
    def __on_creation__(cls, record):
        return checked(record, cls.creationFields)

    @classmethod
    def __on_update__(cls, record):
        patch = checked(record, cls.updateFields)
        return patch


class AccountChecker(Checker):
    creationFields = {
        "name": [check_arg_is_required, check_string],
        "password": [check_arg_is_required, check_string],
        "email": [check_arg_is_required, check_email],
        "fbid": [check_string],
        "diets": [check_valid_diets],
        "dietary_restrictions": [check_valid_dietary_restrictions],
        "cuisine_preferences": [check_valid_cuisines],
    }
    updateFields = {
        "name": [check_string],
        "password": [check_string],
        "email": [check_email],
        "fbid": [check_string],
        "diets": [check_valid_diets],
        "dietary_restrictions": [check_valid_dietary_restrictions],
        "cuisine_preferences": [check_valid_cuisines],
    }


class MealChecker(Checker):
    creationFields = {
        "category": [check_arg_is_required, check_category],
    }
    updateFields = {
        "category": [check_category],
    }


class NutritionChecker(Checker):
    creationFields = {
        "food_id": [check_arg_is_required, check_string],
        "kcal": [check_float],
        "protein_g": [check_float],
        "total_fat_g": [check_float],
        "total_carb_g": [check_float],
        "total_carb_g": [check_float],
        "total_diet_fiber_g": [check_float],
        "calcium_mg": [check_float],
        "iron_mg": [check_float],
        "magnesium_mg": [check_float],
        "phosphorus_mg": [check_float],
        "potassium_mg": [check_float],
        "sodium_mg": [check_float],
        "zinc_mg": [check_float],
        "copper_mg": [check_float],
        "manganese_mg": [check_float],
        "selenium_mcg": [check_float],
        "vitamin_c_mg": [check_float],
        "thiamin_mg": [check_float],
        "riboflavin_mg": [check_float],
        "niacin_mg": [check_float],
        "pantothenic_acid_mg": [check_float],
        "vitamin_b6_mg": [check_float],
        "total_folate_mcg": [check_float],
        "vitamin_b12_mcg": [check_float],
        "vitamin_d_mcg": [check_float],
        "vitamin_e_mg": [check_float],
        "vitamin_k_mcg": [check_float],
        "total_sat_fat_g": [check_float],
        "total_monounsat_fat_g": [check_float],
        "total_poly_unsat_fat_g": [check_float],
        "total_trans_fat_g": [check_float],
        "cholesterol_mg": [check_float],
        "total_sugar_g": [check_float],
        "omega_3_fatty_acids_g": [check_float],
    }
    updateFields = {}

    @classmethod
    def __on_creation__(cls, record, food_id):
        record["food_id"] = food_id
        return checked(record, cls.creationFields, convert_missing_nut_to_zero=True)


class FoodDetailChecker(Checker):
    creationFields = {
        "food_id": [check_arg_is_required, check_string],
        "food_desc": [check_arg_is_required, check_string],
        "barcode": [check_barcode],
        "brand": [check_string],
    }
    updateFields = {}

    @classmethod
    def __on_creation__(cls, record, food_id):
        record["food_id"] = food_id
        return checked(record, cls.creationFields)


class FoodUnitChecker(Checker):
    creationFields = {
        "food_id": [check_arg_is_required, check_string],
        "unit_desc": [check_arg_is_required, check_string],
        "grams_per_unit": [check_arg_is_required, check_float],
    }
    updateFields = {}

    @classmethod
    def __on_creation__(cls, record, food_id):
        record["food_id"] = food_id
        return checked(record, cls.creationFields)


class MealLogChecker(Checker):
    creationFields = {"raw_text": [check_arg_is_required, check_string]}
    updateFields = {"raw_text": [check_string]}


class RecipeChecker(Checker):
    creationFields = {}
    updateFields = {}


class SavedRecipeChecker(Checker):
    creationFields = {}
    updateFields = {}