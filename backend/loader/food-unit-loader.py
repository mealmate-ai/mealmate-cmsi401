import csv
import re
import sys

UNIT_SOURCE = "food_unit.csv"
with open(UNIT_SOURCE, "r+", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    seen = set()
    next(reader)
    for row in reader:
        if (row[0], row[1]) in seen:
            continue

        food_id = row[0]
        unit_desc = row[1]
        unit_desc = unit_desc.replace("'", "''")
        grams_per_unit = row[2]

        if 'ONZ' in unit_desc:
            print(
                f"INSERT INTO food_unit VALUES('{food_id}', '{unit_desc}', {grams_per_unit});"
            )
            seen.add((row[0], unit_desc))
            unit_desc = unit_desc.replace('ONZ', 'oz')
        print(
            f"INSERT INTO food_unit VALUES('{food_id}', '{unit_desc}', {grams_per_unit});"
        )
       
        seen.add((row[0], unit_desc))
