from sqlalchemy.exc import IntegrityError
from dals.models import db, UserSession


def create_user_session(session_details):
    try:
        user_session = UserSession(**session_details)
        db.session.add(user_session)
        db.session.commit()

        return user_session.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def update_user_session(session_id, session_patch):
    sesion = UserSession.get_session_by_id(session_id)
    for key, value in session_patch.items():
        setattr(sesion, key, value)
    db.session.commit()
    return sesion.full_view()
