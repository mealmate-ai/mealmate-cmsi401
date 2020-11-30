from checks.helpers import *
from daily_bites_app.errors import BadArgumentError


def checked():
    pass


class Checker:
    @classmethod
    def __on_creation__(cls, record):
        return checked()

    @classmethod
    def __on_update__(cls, record):
        patch = checked()
        return patch
