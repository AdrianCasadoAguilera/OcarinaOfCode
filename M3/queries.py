import db, screen as scr
query_1 = "SELECT count(distinct user_name) FROM game;"

query_2 = "SELECT user_name, count(*) from game group by user_name;"

query_3 = """SELECT
    wu.game_id,
    g.user_name,
    wu.weapon_name,
    SUM(wu.quantity_used) AS total_armas_gastadas
FROM
    weapons_used wu
JOIN game g ON wu.game_id = g.game_id
GROUP BY
    wu.game_id, g.user_name, wu.weapon_name
ORDER BY
    wu.game_id, g.user_name, total_armas_gastadas DESC;"""

query_4 = """SELECT
    fu.game_id,
    g.user_name,
    fu.food_name,
    SUM(fu.quantity_used) AS total_comida_consumida
FROM
    food_used fu
JOIN game g ON fu.game_id = g.game_id
GROUP BY
    fu.game_id, g.user_name, fu.food_name
ORDER BY
    fu.game_id, g.user_name, total_comida_consumida DESC;"""

query_5 = """SELECT
    AVG(blood_moon_appearances) AS media_blood_moons
FROM
    game;"""

query_6 = """SELECT
    user_name,
    blood_moon_appearances,
    created_at
FROM
    game
ORDER BY
    blood_moon_appearances DESC
LIMIT 1;"""


def menu_queries():
    while(True):
        scr.clear_screen()
        try:
            print("""
1. Usuaris que han jugat
2. Quantitat de partides jugades per cada usuari
3. Armes usades per cada usuari i dades de la partida on n'ha gastat més
4. Menjar consumit per cada usuari i dades de la partida on n'ha consumit més
5. Estadística de "blood moons" 
6. Sortir """)
            
            option = int(input("Escull una opció: "))

            if option == 1:
                db.cur.execute(query_1)
                rst = db.cur.fetchall()
                for i in rst:
                    print(i)
                input("Prem Enter per a continuar")
            elif option == 2:
                db.cur.execute(query_2)
                rst = db.cur.fetchall()
                for i in rst:
                    print(i)
                input("Prem Enter per a continuar")
            elif option == 3:
                db.cur.execute(query_3)
                rst = db.cur.fetchall()
                for i in rst:
                    print(i)
                input("Prem Enter per a continuar")
            elif option == 4:
                db.cur.execute(query_4)
                rst = db.cur.fetchall()
                for i in rst:
                    print(i)
                input("Prem Enter per a continuar")
            elif option == 5:
                db.cur.execute(query_5)
                rst = db.cur.fetchall()
                db.cur.execute(query_6)
                rst2 = db.cur.fetchall()
                print(f"Mitjana de blood moons: {rst[0][0]}\n")
                print(f"Partida amb més blood_moons")
                print("user_name".ljust(15),"| created_at".ljust(15),"| blood_moons")
                print(f"{rst2[0][0]}".ljust(15),f"| {rst2[0][2]}".ljust(15),f"| {rst2[0][1]}")
                input("Prem Enter per a continuar")
            elif option == 6:
                break

        except:
            print("Escull una opció de 1 a 6!")
        