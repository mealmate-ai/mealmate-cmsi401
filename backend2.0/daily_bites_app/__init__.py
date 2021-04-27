from datetime import datetime, date
from decimal import Decimal
from flask import Flask, request, Response, jsonify
from flask.json import JSONEncoder
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.debug = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DAILY_BITES_DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True