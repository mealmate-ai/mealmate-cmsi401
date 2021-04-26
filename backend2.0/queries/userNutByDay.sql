select *
from meal m left join food f on f.meal_id = m.id left join nut_per_100_gram n on n.food_id = f.food_id;