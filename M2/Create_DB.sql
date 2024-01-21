DROP DATABASE IF EXISTS zelda;
CREATE DATABASE IF NOT EXISTS zelda;
USE zelda;

-- Tabla principal de juegos
CREATE TABLE game (
    game_id INT,
    user_name VARCHAR(50),
    last_connected DATETIME,
    hearts_remaining INT,
    max_hearts INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region VARCHAR(50),
    created_at DATETIME 
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
    lives_remaining INT,
    quantity INT
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
CREATE TABLE sanctuaries (
    game_id INT,
    region VARCHAR(50),
    num INT,
    opened BOOLEAN,
	xpos FLOAT,
    ypos FLOAT
);

-- Tabla de cofres abiertos (chests_opened)
CREATE TABLE chests (
    game_id INT,
    region VARCHAR(50),
    num INT,
    opened BOOLEAN,
    xpos FLOAT,
    ypos FLOAT
);

CREATE TABLE trees (
	game_id INT,
    region VARCHAR(50),
	num INT,
    xpos INT,
    ypos INT,
    times_hit INT,
    waiting_time INT
);

CREATE TABLE weapons_used (
	weapon_name VARCHAR(50),
    game_id INT,
    quantity_used INT
);

CREATE TABLE food_used (
	food_name VARCHAR(50),
    game_id INT,
    quantity_used INT
);