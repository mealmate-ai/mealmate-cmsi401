from services import dal
from checks import AccountChecker
from datetime import datetime
import uuid
from dals.models import Account
from passlib.hash import pbkdf2_sha256


def signup(account_info):
    account = AccountChecker.__on_creation__(account_info)
    accountExists = Account.get_account_by_email(account["email"]) is not None
    if accountExists:
        return {"message": f"This email already exists: {account['email']}"}, 409
    account["id"] = str(uuid.uuid4())
    account["date_created"] = datetime.today().strftime("%Y-%m-%d")
    account["password"] = _encrypt(account["password"])
    return {"account": dal.insert_account(account)}, 201

def login(account_info):
    checkedAccount = AccountChecker.__on_login__(account_info)
    account = Account.get_account_by_email(checkedAccount["email"])
    if not account:
        return {"message": "Email not found in the database"}, 404
    
    if not _verify(checkedAccount["password"], account.password):
        return {"message": "Incorrect password provided, please try again"}, 401
    
    token = account.encode_auth_token(account.id)
    accountIdFromToken = account.decode_auth_token(token)
    print(token, type(token), accountIdFromToken)
    # TODO : ADD LOGIN TOKEN
    return {"message": account.full_view(), "token": token}, 201


def create_account(account_info):
    account = AccountChecker.__on_creation__(account_info)
    account["id"] = str(uuid.uuid4())
    account["date_created"] = datetime.today().strftime("%Y-%m-%d")
    return {"account": dal.insert_account(account)}, 201


def get_account(account_id):
    account = Account.get_account_by_id(account_id)
    return None if account is None else account.full_view()


def update_account(account_id, patch_content):
    patch = AccountChecker.__on_update__(patch_content)
    if not patch:
        return {"message": "No fields to update from arguments"}, 400
    updated_account = dal.update_account(account_id, patch)
    return {"account": updated_account}, 200


def remove_account(account_id):
    return {"deleted": dal.delete_account(account_id)}, 200


def _encrypt(password_input):
    return pbkdf2_sha256.hash(password_input)

def _verify(password, accountHash):
    return pbkdf2_sha256.verify(password, accountHash)