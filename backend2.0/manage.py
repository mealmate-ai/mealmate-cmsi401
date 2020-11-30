from datetime import datetime
import re
import json

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import text
from daily_bites_app.routes import app
from dals import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()