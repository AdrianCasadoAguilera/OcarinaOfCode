import mysql.connector, data

connection = mysql.connector.connect(user='OcarinaOfCode',password='1234',host='127.0.0.1',database='zelda')

cur = connection.cursor()


# QUERIES FROM GAME TABLE

def user_name(id):
    cur.execute(f"SELECT user_name FROM game WHERE game_id={id}")
    name = cur.fetchall()
    return name[0][0]

def actual_hearts(id):
    cur.execute(f"SELECT hearts_remaining FROM game WHERE game_id={id}")
    act_hearts = cur.fetchall()
    return act_hearts[0][0]

def name(id):
    cur.execute(f"SELECT user_name FROM game WHERE game_id={id}")
    usr_name = cur.fetchall()
    return usr_name[0][0]

def max_hearts(id):
    cur.execute(f"SELECT max_hearts FROM game WHERE game_id={id}")
    hearts = cur.fetchall()
    return hearts[0][0]

def region(id):
    cur.execute(f"SELECT region from game WHERE game_id = {id};")
    region = cur.fetchall()
    return region[0][0]

def blood_moon_countdown(id):
    cur.execute(f"SELECT blood_moon_countdown from game WHERE game_id = {id};")
    countdown = cur.fetchall()
    return countdown[0][0]

def weapons_equiped(id):
    cur.execute(f"SELECT weapon_name FROM weapons WHERE equipped=1 and game_id={id};")
    weapons = cur.fetchall()
    if(len(weapons)==0):
        return ["",""]
    elif(len(weapons)==1):
        return [weapons[0][0],""]
    weapons_list = []
    for i in range(2):
        weapons_list.append(weapons[i][0])
    return weapons_list

def food_totals(id):
    food_names = ["Vegetable","Fish","Meat","Salad","Pescatarian","Roasted"]
    dic = {}
    for food_name in food_names:
        cur.execute(f'SELECT quantity FROM foods WHERE game_id={id} and food_name="{food_name}"')
        food = cur.fetchall()
        if(len(food)>0):
            dic[food_name] = food[0][0]
        else:
            dic[food_name] = 0
    return dic

def weapon_quantity(id):
    weapon_names = ["Wood Sword", "Sword", "Wood Shield", "Shield"]
    weapon_dic = {}
    for weapon_name in weapon_names:
        cur.execute(f'SELECT quantity FROM weapons WHERE game_id={id} and weapon_name="{weapon_name}"')
        weapon = cur.fetchall()
        if(len(weapon)>0):
            weapon_dic[weapon_name] = weapon[0][0]
        else:
            weapon_dic[weapon_name] = 0
    return weapon_dic

def weapon_durability(id):
    weapon_names = ["Wood Sword", "Sword", "Wood Shield", "Shield"]
    weapons = {}
    for weapon_name in weapon_names:
        cur.execute(f'SELECT lives_remaining FROM weapons WHERE game_id={id} and weapon_name="{weapon_name}"')
        weapon = cur.fetchall()
        if(len(weapon)==0):
            weapon_name_list = weapon_name.split()
            if(weapon_name_list[0] == "Wood"):
                weapons[weapon_name] = 5
            else:
                weapons[weapon_name] = 9
        else:
            weapons[weapon_name] = weapon[0][0]
    return weapons
 
def region(id):
    cur.execute(f"SELECT region FROM game WHERE game_id = {id}")
    rst = cur.fetchall()
    return rst[0][0]

def is_equipped(id, weapon):
    cur.execute(f'SELECT equipped FROM weapons WHERE game_id={id} and weapon_name="{weapon}"')
    equipped_weapon = cur.fetchall()
    if(len(equipped_weapon)==0):
        return 0
    else:
        if equipped_weapon[0][0] == 1:
            return 1
        else:
            return 0


def change_map(selected_map, id):
    cur.execute(f'UPDATE game SET region = "{selected_map}" WHERE game_id = {id}')
    cur.execute("commit")

def update_database():
    character = data.data['character']
    game_query = f"""
        UPDATE game
        SET user_name = '{character['user_name']}',
            hearts_remaining = {character['hearts_remaining']},
            max_hearts = {character['max_hearts']},
            region = '{character['region']}',
            blood_moon_countdown = {character['blood_moon_countdown']}
        WHERE game_id = {character['game_id']}
    """
    cur.execute(game_query)
    
    for food_name, quantity in data.data['foods'].items():
        foods_query = f"""
            UPDATE foods
            SET quantity = {quantity}
            WHERE game_id = {character['game_id']} AND food_name = '{food_name}'
        """
        cur.execute(foods_query)

    for weapon_name, weapon_data in data.data['weapons'].items():
        weapons_query = f"""
            UPDATE weapons
            SET quantity = {weapon_data['quantity']},
                equipped = {weapon_data['equipped']},
                lives_remaining = {weapon_data['durability']}
            WHERE game_id = {character['game_id']} AND weapon_name = '{weapon_name}'
        """
        cur.execute(weapons_query)
        
    for region, region_data in data.locations.items():
        for enemy_num, enemy_info in region_data['enemies'].items():
            enemies_query = f"""
                UPDATE enemies
                SET xpos = {enemy_info[1][0]},
                    ypos = {enemy_info[1][1]},
                    lifes_remaining = {enemy_info[0]}
                WHERE game_id = {character['game_id']} AND region = '{region}' AND num = {enemy_num}
            """
            cur.execute(enemies_query)

        for chest_num, chest_data in region_data['chests'].items():
            chests_query = f"""
                UPDATE chests
                SET opened = {chest_data[0]},
                    xpos = {chest_data[1][0]},
                    ypos = {chest_data[1][1]}
                WHERE game_id = {character['game_id']} AND region = '{region}' AND num = {chest_num}
            """
            cur.execute(chests_query)

        for sanct_num, sanct_data in region_data['sanctuaries'].items():
            sanct_query = f"""
                UPDATE sanctuaries
                SET opened = {sanct_data[0]},
                    xpos = {sanct_data[1][0]},
                    ypos = {sanct_data[1][1]}
                WHERE game_id = {character['game_id']} AND region = '{region}' AND num = {sanct_num}
            """
            cur.execute(sanct_query)

        for tree_num, tree_info in region_data['trees'].items():
            if(tree_info[0]>0):
                tree_query = f"""
                    UPDATE trees
                    SET xpos = {tree_info[1][0]},
                        ypos = {tree_info[1][1]},
                        times_hit = {tree_info[0]},
                        waiting_time = 0
                    WHERE game_id = {character['game_id']} AND region = '{region}' AND num = {tree_num}"""
            else:
                tree_query = f"""
                    UPDATE trees
                    SET xpos = {tree_info[1][0]},
                        ypos = {tree_info[1][1]},
                        times_hit = 0,
                        waiting_time = {-tree_info[0]}
                    WHERE game_id = {character['game_id']} AND region = '{region}' AND num = {tree_num}"""
            cur.execute(tree_query)

        game_query = f"""
            UPDATE game
            SET fishing = {region_data['fishing']}
            WHERE game_id = {character['game_id']} AND region = '{region}'
        """
        cur.execute(game_query)


    connection.commit()

def insert_initial_data(game_id):

    # Insertar datos en la tabla foods
    for food_name, quantity in data.data['foods'].items():
        cur.execute("""
            INSERT INTO foods (food_name, game_id, quantity)
            VALUES (%s, %s, %s)
        """, (food_name, game_id[0][0], quantity))

    # Insertar datos en la tabla weapons
    for weapon_name, weapon_data in data.data['weapons'].items():
        cur.execute("""
            INSERT INTO weapons (weapon_name, game_id, equipped, lives_remaining, quantity)
            VALUES (%s, %s, %s, %s, %s)
        """, (weapon_name, game_id[0][0], weapon_data['equipped'], weapon_data['durability'], weapon_data['quantity']))

    # Insertar datos en la tabla enemies
    for region, region_data in data.locations.items():
        for enemy_num, enemy_info in region_data.get('enemies', {}).items():
            cur.execute("""
                INSERT INTO enemies (game_id, region, num, xpos, ypos, lifes_remaining)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (game_id[0][0], region, enemy_num, enemy_info[1][0], enemy_info[1][1], enemy_info[0]))

    # Insertar datos en la tabla trees
    for region, region_data in data.locations.items():
        for tree_num, tree_info in region_data.get('trees', {}).items():
            cur.execute("""
                INSERT INTO trees (game_id, region, num, xpos, ypos, times_hit, waiting_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (game_id[0][0], region, tree_num, tree_info[1][0], tree_info[1][1], tree_info[0], 0))

    # Insertar datos en la tabla chests
    for region, region_data in data.locations.items():
        for chest_num, chest_info in region_data.get('chests', {}).items():
            cur.execute("""
                INSERT INTO chests (game_id, region, num, opened, xpos, ypos)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (game_id[0][0], region, chest_num, chest_info[0], chest_info[1][0], chest_info[1][1]))

    # Insertar datos en la tabla sanctuaries
    for region, region_data in data.locations.items():
        for sanctuary_num, sanctuary_info in region_data.get('sanctuaries', {}).items():
            cur.execute("""
                INSERT INTO sanctuaries (game_id, region, num, opened, xpos, ypos)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (game_id[0][0], region, sanctuary_num, sanctuary_info[0], sanctuary_info[1][0], sanctuary_info[1][1]))

    for food_name, quantity in data.data['foods'].items():
        cur.execute("""
            INSERT INTO food_used (food_name, game_id, quantity_used)
            VALUES (%s, %s, %s)
        """, (food_name, game_id[0][0], 0))

    # Insertar datos en la tabla weapons
    for weapon_name, weapon_data in data.data['weapons'].items():
        cur.execute("""
            INSERT INTO weapons_used (weapon_name, game_id, quantity_used)
            VALUES (%s, %s, %s)
        """, (weapon_name, game_id[0][0], 0))


    # Confirmar los cambios
    connection.commit()