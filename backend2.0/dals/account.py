from sqlalchemy.exc import IntegrityError
from dals.models import db, Account, Meal
from datetime import datetime


def insert_account(account_args):
    try:
        inserted_account = Account(**account_args)
        db.session.add(inserted_account)
        db.session.commit()
        return inserted_account
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_account_by_id(account_id):
    account = Account.get_account_by_id(account_id)
    return account.full_view()


def update_account(account_id, account_patch):
    account = Account.get_account_by_id(account_id)
    for key, value in account_patch.items():
        setattr(account, key, value)
    db.session.commit()
    return account.full_view()

def update_login_date(account):
    try: 
        setattr(account, 'most_recent_login', datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise

def delete_account(account_id):
    account = Account.get_account_by_id(account_id)
    if len(account) < 1:
        return 'Invalid account_id provided'
    db.session.delete(account)
    db.session.commit()
    return True

def get_last_logout(account_id):
    account = Account.get_account_by_id(account_id)
    return None if account is None else account.last_logout

def update_last_logout(account_id, time):
    account = Account.get_account_by_id(account_id)
    try:
        setattr(account, 'last_logout', time)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise