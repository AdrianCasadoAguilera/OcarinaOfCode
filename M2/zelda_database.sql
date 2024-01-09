DROP DATABASE IF EXISTS zelda;
CREATE DATABASE IF NOT EXISTS zelda;
USE zelda;

-- Tabla principal de juegos
CREATE TABLE game (
    game_id INT,
    user_name VARCHAR(50),
    date_started DATETIME,
    last_connected DATETIME,
    hearts_remaining INT,
    max_hearts INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(50)
);

-- Tabla de comidas
CREATE TABLE foods (
    food_name VARCHAR(50),
    game_id INT,
    quantity INT
);

-- Tabla de armas del juego
CREATE TABLE weapons (
    weapon_name VARCHAR(50),
    game_id INT,
    equipped BOOLEAN,
    lives_remaining INT
);

-- Tabla de enemigos (enemies)
CREATE TABLE enemies (
    game_id INT,
    region VARCHAR(50),
    num INT,
    xpos FLOAT,
    ypos FLOAT,
    lifes_remaining INT
);

-- Tabla de santuarios abiertos (sanctuaries_opened)
CREATE TABLE sanctuaries_opened (
    game_id INT,
    region VARCHAR(50),
    num INT,
	xpos FLOAT,
    ypos FLOAT
);

-- Tabla de cofres abiertos (chests_opened)
CREATE TABLE chests_opened (
    game_id INT,
    region VARCHAR(50),
    num INT,
    xpos FLOAT,
    ypos FLOAT
);


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