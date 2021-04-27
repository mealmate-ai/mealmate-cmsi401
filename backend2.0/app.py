""" The Daily Bites Server"""

from daily_bites_app.endpoints import app
from dailybitestagger import get_tags

if __name__ == "__main__":
    print(get_tags('an apple with 2 tablespoons of peanut butter'))
    app.run(host="0.0.0.0", port="8080")
