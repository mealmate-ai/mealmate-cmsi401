from sqlalchemy.exc import IntegrityError
from dals.models import db, Account


def insert_account(account_args):
    try:
        inserted_account = Account(**account_args)
        db.session.add(inserted_account)
        db.session.commit()
        return inserted_account.full_view()
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


def delete_account(account_id):
    account = Account.get_account_by_id(account_id)
    db.session.delete(account)
    db.session.commit()
    return True