from datetime import datetime, date
from decimal import Decimal
import pytz
import boto3
from flask import Flask, request, Response, jsonify
from flask.json import JSONEncoder

app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DAILY_BITES_DB_URL")

