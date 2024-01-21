use zelda;

ALTER TABLE game
MODIFY COLUMN game_id int AUTO_INCREMENT primary key,
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle")) NOT NULL,
MODIFY COLUMN hearts_remaining INT DEFAULT 3,
MODIFY COLUMN max_hearts INT DEFAULT 3,
MODIFY COLUMN fishing BOOLEAN DEFAULT True,
MODIFY COLUMN last_connected DATETIME DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE foods
MODIFY COLUMN food_name VARCHAR(50) CHECK (food_name in ("Vegetable", "Salad", "Pescatarian", "Roasted", "Meat", "Fish")) NOT NULL,
ADD PRIMARY KEY (food_name, game_id),
ADD CONSTRAINT fk_game_foods
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE weapons
MODIFY COLUMN weapon_name VARCHAR(50) CHECK (weapon_name in ("Wood Sword", "Sword", "Wood Shield", "Shield")) NOT NULL,
ADD PRIMARY KEY (weapon_name, game_id),
ADD CONSTRAINT fk_game_weapons
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE enemies
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle")) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
ADD PRIMARY KEY (game_id, region, num),
ADD CONSTRAINT fk_game_enemies
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE sanctuaries
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle")) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
ADD PRIMARY KEY (game_id, num, region),
ADD CONSTRAINT fk_game_sanctuaries
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE chests
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle")) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
ADD PRIMARY KEY (game_id, region, num),
ADD CONSTRAINT fk_game_chests
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE trees
MODIFY COLUMN region VARCHAR(50) CHECK (region in ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle")) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
MODIFY COLUMN times_hit INT DEFAULT 0,
ADD PRIMARY KEY (game_id, region, num),
ADD CONSTRAINT fk_game_trees
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE food_used
MODIFY COLUMN food_name VARCHAR(50) CHECK (food_name in ("Vegetable", "Salad", "Pescatarian", "Roasted", "Meat", "Fish")) NOT NULL,
ADD PRIMARY KEY (game_id, food_name),
ADD CONSTRAINT fk_game_food_used
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;

ALTER TABLE weapons_used
MODIFY COLUMN weapon_name VARCHAR(50) CHECK (weapon_name in ("Wood Sword", "Sword", "Wood Shield", "Shield")) NOT NULL,
ADD PRIMARY KEY (game_id, weapon_name),
ADD CONSTRAINT fk_game_weapons_used
FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE;