# Daily Bites Routes

## `/add-account`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| name | string | no | Sara Smith | name of user to create the account for |
| email | string | yes | sarasmith987@gmail.com | email of user to create the account for |

## `/get-account/<account_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| account_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the account to retrieve |

## `/update-account/<account_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| account_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the account to update |
| name | string | yes | Sara Smith | name of user to create the account for |
| email | string | yes | sarasmith987@gmail.com | email of user to create the account for |
| diets | string | yes | Keto,Gluten Free | list of diets the user follows |
| dietary_restrictions | string | yes | Soy | list of intolerances the user has |
| cuisine_preferences | string | yes | Mexican,Mediterranean | list of cuisine preferences |

## `/delete-account/<account_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| account_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the account to delete |

## `/add-meal`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| account_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | user who creates the meal |
| category | string | yes | sarasmith987@gmail.com | category of the meal being logged |

## `/get-meal/<account_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| account_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the user to retrieve meals for |
| date | date (YYYY-MM-DD) | yes | 2020-12-12 | optional query parameter for the date of meals |
| category | string | yes | Lunch | optional category to filter meals |

## `/delete-meal/<meal_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| meal_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the meal to delete |

## `/query-foods`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| query | string | no | peanut butter toast | test representation of food searching for |

## `/query-mv-foods`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| query | string | no | peanut butter toast | test representation of food searching for |

## `/query-barcode/<barcode>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| barcode | string | no | 077890443859 | barcode of food scanning |

## `/log-meal/<meal_id>`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| meal_id | uuid | no | 9831e3a38dcc4eccb9a432146a3a7de9 | id of the meal to delete |
| raw_text | string | no | two tablespoons peanut butter | text representation of user's interaction with the chatbot |

## `/get-random-recipes`

| Parameters | Type | Optional | Example | Description |
| ---------- | ---- | -------- | ------- | ----------- |
| number | int | yes | 12 | number of random recipes to get |

<!-- TODO: add default column -->