from services import dal
from checks import AccountChecker
from datetime import datetime
import uuid
from dals.models import Account


def create_account(account_info):
    account = AccountChecker.__on_creation__(account_info)
    account["id"] = str(uuid.uuid4())
    account["date_created"] = datetime.today().strftime("%Y-%m-%d")
    return {"account": dal.insert_account(account)}, 201


def get_account(account_id):
    account = Account.get_account_by_id(account_id)
    return None if account is None else account.full_view()
