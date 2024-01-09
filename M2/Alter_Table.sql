use zelda;



ALTER TABLE game
MODIFY COLUMN game_id int AUTO_INCREMENT primary key;

ALTER TABLE game
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle"));

ALTER TABLE game
MODIFY COLUMN hearts_remaining INT DEFAULT 3;

ALTER TABLE game
MODIFY COLUMN max_hearts INT DEFAULT 3;

ALTER TABLE foods
MODIFY COLUMN food_name VARCHAR(50) CHECK (food_name in ("Vegetable", "Salad", "Pescatarian", "Roasted", "Meat", "Fish"));

ALTER TABLE weapons
MODIFY COLUMN weapon_name VARCHAR(50) CHECK (weapon_name in ("Wood Sword", "Sword", "Wood Shield", "Shield"));

ALTER TABLE enemies
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle"));

ALTER TABLE sanctuaries_opened
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle"));

ALTER TABLE chests_opened
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle"));

ALTER TABLE foods
ADD PRIMARY KEY (food_name, game_id);

ALTER TABLE foods
ADD CONSTRAINT fk_game_foods
FOREIGN KEY (game_id) REFERENCES game(game_id);

ALTER TABLE weapons
ADD PRIMARY KEY (weapon_name, game_id);

ALTER TABLE weapons
ADD CONSTRAINT fk_game_weapons
FOREIGN KEY (game_id) REFERENCES game(game_id);

ALTER TABLE enemies
ADD PRIMARY KEY (game_id, region, num);

ALTER TABLE enemies
ADD CONSTRAINT fk_game_enemies
FOREIGN KEY (game_id) REFERENCES game(game_id);

ALTER TABLE sanctuaries_opened
ADD PRIMARY KEY (game_id, num, region);

ALTER TABLE sanctuaries_opened
ADD CONSTRAINT fk_game_sanctuaries_opened
FOREIGN KEY (game_id) REFERENCES game(game_id);

ALTER TABLE chests_opened
ADD PRIMARY KEY (game_id, region, num);

ALTER TABLE chests_opened
ADD CONSTRAINT fk_game_chests_opened
FOREIGN KEY (game_id) REFERENCES game(game_id);