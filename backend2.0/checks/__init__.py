from checks.helpers import *
from daily_bites_app.errors import BadArgumentError


def checked(obj, requirements):
    if not isinstance(obj, dict):
        raise BadArgumentError("Invalid arguments provided, JSON required")
    checkedArgs = {}

    for key, constraint in requirements.items():
        value = obj.get(key)

        for check in constraint:
            check(key, value)
        if value is not None:
            checkedArgs[key] = value
            print(checkedArgs)
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
        "email": [check_email],
        "fbid": [check_string],
    }
    updateFields: {
        "name": [check_string],
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
