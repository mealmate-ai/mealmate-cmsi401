import re
from checks.constants import *


def check(condition, message):
    from daily_bites_app.errors import BadArgumentError

    if not condition:
        raise BadArgumentError(message)


def check_arg_is_required(key, value):
    check(value is not None, f"Parameter {key} must be an integer")


def check_integer(key, value):
    check(value is None or isinstance(value, int), f"Parameter {key} must be an integer")


def check_string(key, value):
    check(value is None or isinstance(value, str), f"Parameter {key} must be a string")


def check_boolean(key, value):
    check(value is None or isinstance(value, bool), f"Parameter {key} must be an boolean")


def check_uuid(key, value):
    import uuid

    check(value is None or isinstance(value, uuid.UUID), f"Parameter {key} must be an integer")


def check_date(key, value):
    check(
        value is None or isinstance(value, str) and re.match(r"^\d\d\d\d-\d\d-\d\d+$", value),
        f"Parameter {key} does not look like a date",
    )


def check_email(key, value):
    check(
        value is None or isinstance(value, str),
        f"Parameter {key} does not look like an email",
    )


def check_valid_diets(key, value):
    if value is not None:
        diets = [v.strip() for v in value.split(",")]
        for diet in diets:
            check(
                isinstance(value, str) and diet in SPOONACULAR_DIETS,
                f"Parameter {key} must be a Spoonacular Diet",
            )


def check_valid_dietary_restrictions(key, value):
    if value is not None:
        intolarances = [v.strip() for v in value.split(",")]
        for intolerance in intolarances:
            check(
                isinstance(value, str) and intolerance in SPOONACULAR_INTOLERANCES,
                f"Parameter {key} must be a Spoonacular Intolerance",
            )


def check_valid_cuisines(key, value):
    if value is not None:
        cuisines = [v.strip() for v in value.split(",")]
        for cuisine in cuisines:
            check(
                isinstance(value, str) and cuisine in SPOONACULAR_CUSINES,
                f"Parameter {key} must be a Spoonacular Cuisine",
            )


def check_category(key, value):
    if value is not None:
        check(
            isinstance(value, str) and value in CATEGORIES,
            f"Parameter {key} must be a valid category",
        )
