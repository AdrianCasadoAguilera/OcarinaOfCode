use zelda;

SELECT user_name, count(*) from game group by user_name;

SELECT count(distinct user_name) FROM game;


SELECT 
    wu.game_id,
    g.user_name,
    wu.weapon_name,
    wu.quantity_used,
    g.region,
    g.last_connected
FROM
    weapons_used wu
JOIN game g ON wu.game_id = g.game_id
WHERE
    (wu.game_id, wu.quantity_used) IN (
        SELECT
            game_id,
            MAX(quantity_used) AS max_quantity_used
        FROM
            weapons_used
        GROUP BY
            game_id
    );

