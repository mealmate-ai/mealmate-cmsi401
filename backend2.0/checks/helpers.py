import re


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
