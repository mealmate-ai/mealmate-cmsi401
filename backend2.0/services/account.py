from services import dal
from checks import AccountChecker
from datetime import datetime
import uuid


def create_account(account_info):
    print(account_info)
    account = AccountChecker.__on_creation__(account_info)
    print(account)
    account["id"] = str(uuid.uuid4())
    account["date_created"] = datetime.today().strftime("%Y-%m-%d")
    return {"account": dal.insert_account(account)}, 201
