# How many total Characters are there?

SELECT * FROM charactercreator_character;
# Answer: 302

# How many of each specific subclass?
SELECT * FROM charactercreator_mage;
# Answer: 108
SELECT * FROM charactercreator_thief;
# ANSWER: 68
SELECT * FROM charactercreator_cleric;
# ANSWER: 75
SELECT * FROM charactercreator_fighter;
# ANSWER: 68
SELECT * FROM charactercreator_necromancer;
# ANSWER: 11

# How many total Items?
SELECT * FROM charactercreator_inventory;
# ANSWER: 898

# How many of the Items are weapons? How many are not?
SELECT * FROM armory_item;
# ANSWER: 174

# How many Items does each character have? (Return first 20 rows)

# How many Weapons does each character have? (Return first 20 rows)
SELECT ccc.character_id, cci.character_id, ai.item_id
FROM charactercreator_character as ccc,
charactercreator_character_inventory as cci,
armory_item as ai
WHERE ccc.character_id = cci.character_id
AND cci.item_id = ai.item_id
LIMIT 20

# On average, how many Items does each Character have?
SELECT AVG(item_id)
FROM charactercreator_character_inventory as cci
# 89.1781737193764
