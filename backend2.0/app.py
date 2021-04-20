""" The Daily Bites Server"""

from daily_bites_app.endpoints import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
