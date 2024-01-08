DROP DATABASE IF EXISTS zelda;
CREATE DATABASE IF NOT EXISTS zelda;
USE zelda;

-- Tabla principal de juegos
CREATE TABLE game (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    date_started DATE,
    hearts_remaining INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(50)
);

-- Tabla de comidas
CREATE TABLE foods (
    food_name VARCHAR(50) PRIMARY KEY,
    game_id INT,
    quantity INT,
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

-- Tabla de armas del juego
CREATE TABLE weapons (
    weapon_name VARCHAR(50) PRIMARY KEY,
    game_id INT,
    equipped BOOLEAN,
    lives_remaining INT,
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

-- Tabla de enemigos (enemies)
CREATE TABLE enemies (
    game_id INT,
    region VARCHAR(50),
    num INT,
    xpos FLOAT,
    ypos FLOAT,
    lifes_remaining INT,
    PRIMARY KEY (region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

-- Tabla de santuarios abiertos (sanctuaries_opened)
CREATE TABLE sanctuaries_opened (
    game_id INT,
    region VARCHAR(50),
    num INT,
    xpos FLOAT,
    ypos FLOAT,
    PRIMARY KEY (region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

-- Tabla de cofres abiertos (chests_opened)
CREATE TABLE chests_opened (
    game_id INT,
    region VARCHAR(50),
    num INT,
    xpos FLOAT,
    ypos FLOAT,
    PRIMARY KEY (region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);