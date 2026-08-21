% Disease and recommended diet

diet(diabetes, recommended, [vegetables, whole_grains, legumes]).
diet(diabetes, avoid, [sugary_drinks, sweets, refined_sugar]).

diet(hypertension, recommended, [fruits, vegetables, whole_grains]).
diet(hypertension, avoid, [salty_foods, processed_foods, excess_salt]).

diet(anemia, recommended, [spinach, beans, lentils, iron_rich_foods]).
diet(anemia, avoid, [excess_tea, excess_coffee]).

diet(obesity, recommended, [vegetables, fruits, whole_grains]).
diet(obesity, avoid, [fast_food, sugary_drinks, fried_foods]).

suggest_diet(Disease, Recommended, Avoid) :-
    diet(Disease, recommended, Recommended),
    diet(Disease, avoid, Avoid).
