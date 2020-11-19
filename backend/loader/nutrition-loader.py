import csv
import re
import sys

NUTR_SOURCE = "nut_per_100_gram.csv"
with open(NUTR_SOURCE, "r+", encoding="iso-8859-1") as f:
    reader = csv.reader(f)
    next(reader)
    seen = set()
    for row in reader:
        if row[0] in seen:
            continue
        food_id = row[0]
        kcal = row[1]
        protein_g = row[2]
        total_fat_g = row[3]
        total_carb_g = row[4]
        # add more rows
        total_diet_fiber_g = row[5]
        calcium_mg = row[6]
        iron_mg = row[7]
        magnesium_mg = row[8]
        phosphorus_mg = row[9]
        potassium_mg = row[10]
        sodium_mg = row[11]
        zinc_mg = row[12]
        copper_mg = row[13]
        manganese_mg = row[14]
        selenium_mcg = row[15]
        vitamin_c_mg = row[16]
        thiamin_mg = row[17]
        riboflavin_mg = row[18]
        niacin_mg = row[19]
        pantothenic_acid_mg = row[20]
        vitamin_b6_mg = row[21]
        total_folate_mcg = row[22]
        vitamin_b12_mcg = row[23]
        vitamin_d_mcg = row[24]
        vitamin_e_mg = row[25]
        vitamin_k_mcg = row[26]
        total_sat_fat_g = row[27]
        total_monounsat_fat_g = row[28]
        total_poly_unsat_fat_g = row[29]
        total_trans_fat_g = row[30]
        cholesterol_mg = row[31]
        total_sugar_g = row[32]
        omega_3_fatty_acids_g = row[33]
        print(
            f"""
            INSERT INTO nut_per_100_gram VALUES('
                {food_id}',
                {kcal},
                {protein_g},
                {total_fat_g},
                {total_carb_g},
                {total_diet_fiber_g},
                {calcium_mg},
                {iron_mg},
                {magnesium_mg},
                {phosphorus_mg},
                {potassium_mg},
                {sodium_mg},
                {zinc_mg},
                {copper_mg},
                {manganese_mg},
                {selenium_mcg},
                {vitamin_c_mg},
                {thiamin_mg},
                {riboflavin_mg},
                {niacin_mg},
                {pantothenic_acid_mg},
                {vitamin_b6_mg},
                {total_folate_mcg},
                {vitamin_b12_mcg},
                {vitamin_d_mcg},
                {vitamin_e_mg},
                {vitamin_k_mcg},
                {total_sat_fat_g},
                {total_monounsat_fat_g},
                {total_poly_unsat_fat_g},
                {total_trans_fat_g},
                {cholesterol_mg},
                {total_sugar_g},
                {omega_3_fatty_acids_g}
            );
            """
        )
        seen.add(food_id)
