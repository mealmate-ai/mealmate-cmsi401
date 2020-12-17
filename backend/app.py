import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DAILY_BITES_DB_URL")
    db.init_app(app)

    return app


app = create_app()
# from routes import hello
with app.app_context():
    import routes

    db.create_all()

if __name__ == "__main__":
    app.debug = True
    app.run()