import csv
import re
import sys

UNIT_SOURCE = "food_unit.csv"
with open(UNIT_SOURCE, "r+", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    seen = set()
    next(reader)