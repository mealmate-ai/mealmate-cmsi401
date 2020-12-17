from datetime import datetime, date
from decimal import Decimal
from flask import Flask, request, Response, jsonify
from flask.json import JSONEncoder
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("LOCAL_DB_URL")
