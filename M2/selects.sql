use zelda;

SELECT user_name, count(*) from game group by user_name;

SELECT count(distinct user_name) FROM game;