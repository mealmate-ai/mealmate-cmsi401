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
