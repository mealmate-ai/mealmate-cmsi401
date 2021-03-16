from services import dal
from datetime import datetime, timedelta
import jwt
import os
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

token_required = auth.login_required

@auth.verify_token
def verify_token(token):
    try:
        payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
