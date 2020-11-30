from flask import g
from daily_bites_app import app


@app.route("/", methods=["GET"])
def hello():
    return {"message": "Hello"}, 200
