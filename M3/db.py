import mysql.connector

connection = mysql.connector.connect(user='OcarinaOfCode',password='1234',host='127.0.0.1',database='zelda')

cur = connection.cursor()


# QUERIES FROM GAME TABLE

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

def weapons_equiped(id):
    cur.execute(f"SELECT weapon_name FROM weapons WHERE equipped=1 and game_id={id};")
    weapons = cur.fetchall()
    if(len(weapons)<2):
        return [weapons[0][0],""]
    weapons_list = []
    for i in range(2):
        weapons_list.append(weapons[i][0])
    return weapons_list

def food_totals(id):
    food_names = ["Vegetables","Fish","Meat","Salads","Pescatarian","Roasted"]
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

def equipped(id, weapon):
    cur.execute(f'SELECT equipped FROM weapons WHERE game_id={id} and weapon_name="{weapon}"')
    equipped_weapon = cur.fetchall()
    if equipped_weapon != 0:
        return "(equipped)"
    else:
        if equipped_weapon[0][0] == 1:
            return "(equipped)"
        else:
            return " "


