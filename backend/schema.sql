CREATE TABLE account (
    id VARCHAR PRIMARY KEY,
    date_created DATE,
    name VARCHAR,
    email VARCHAR
);

CREATE TABLE meal (
    meal_id INT PRIMARY KEY,
    account_id VARCHAR REFERENCES account(id),
    date_logged DATE,
    category VARCHAR
);

CREATE TABLE nut_per_100_gram (
    food_id VARCHAR PRIMARY KEY,
    kcal FLOAT, 
    protein_g FLOAT, 
    total_fat_g FLOAT, 
    total_carb_g FLOAT
);

CREATE TABLE food_unit (
    food_id VARCHAR REFERENCES nut_per_100_gram(food_id),
    unit_desc VARCHAR,
    grams_per_unit FLOAT,
    PRIMARY KEY (food_id, unit_desc)
);

CREATE TABLE food (
    meal_id INT REFERENCES meal(meal_id),
    food_id VARCHAR REFERENCES nut_per_100_gram(food_id),
    log_id INT, 
    food_desc VARCHAR,
    food_unit VARCHAR, 
    food_quantity VARCHAR,
    PRIMARY KEY(meal_id, food_id)  
);

CREATE TABLE meal_log (
    meal_id INT, 
    log_id INT,
    raw_text VARCHAR,
    PRIMARY KEY(meal_id, log_id)  
);

CREATE TABLE food_detail (
    food_id VARCHAR PRIMARY KEY REFERENCES nut_per_100_gram(food_id),
    food_desc VARCHAR,
    barcode VARCHAR,
    brand VARCHAR,
    food_group VARCHAR,
    ingredient_list VARCHAR
);

CREATE TABLE recipe (
    recipe_id INT PRIMARY KEY,
    title VARCHAR,
    recipe_desc VARCHAR,
    recipe_ingredients VARCHAR,
    recipe_instructions VARCHAR
);

CREATE TABLE saved_recipe (
    recipe_id INT REFERENCES recipe(recipe_id),
    account_id VARCHAR REFERENCES account(id),
    date_saved DATE,
    PRIMARY KEY(recipe_id, account_id)  
);

-- TABLES TO CONSIDER ADDING: food_lookup, foodid_vecs, token_vecs