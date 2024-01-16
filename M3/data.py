import db,maps
# Working on this dictionary

data = {}

locations = {
    "Hyrule": {
        "enemies" : {
            1 : [1,[20,8]],
            2 : [9,[25,4]]
        },
        "trees" : {
            1 : [4,[3,5]],
            2 : [4,[8,45]],
            3 : [4,[7,47]]
        },
        "chests": {
            1 : [1,[8,47]]
        },
        "fishing" : 1
        },
    "Death Mountain" : {
        "enemies":{
            1 : [2,[13,4]],
            2 : [2,[51,3]]
        },
        "trees" : {
            1 : [4,[19,7]],
            2 : [4,[18,8]],
            3 : [4,[18,9]]
        },
        "chests": {
            1 : [1,[7,35]]
        },
        "fishing" : 1
    },
    "Gerudo": {
        "enemies": {
            1: [1, [2, 3]],
            2: [2, [37, 5]]
        },
        "trees" : {
            1 : [4,[5,8]],
            2 : [4,[29,2]],
            3 : [4,[30,2]],
            4 : [4,[31,2]],
            5 : [4,[31,3]],
            6 : [4,[32,3]]
        },
        "chests": {
            1 : [1,[0,51]],
            2 : [1,[8,7]]
        },
        "fishing" : 1
    },
    "Necluda" : {
        "enemies" : {
            1 : [1,[10,2]],
            2 : [2,[38,6]]
        },
        "trees" : {
            1 : [4,[15,6]],
            2 : [4,[14,7]],
            3 : [4,[15,8]],
            4 : [4,[38,2]],
            5 : [4,[37,2]],
            6 : [4,[35,3]],
            7 : [4,[36,3]]
        },
        "chests": {
            1 : [1,[0,21]],
            2 : [1,[1,50]],
            3 : [1,[8,22]]
        },
        "fishing" : 1
    }
}

def initialize_data(id,usr_name):
    global data
    data = {
         "character" : {
            "game_id" : id,
            "user_name" : usr_name,
            "position" : [11,7],
            "hearts_remaining" : 3,
            "max_hearts" : 3,
            "region" : "Hyrule",
            "blood_moon_countdown" : 25
        },
        "foods" : {
            "Meat" : 0,
            "Fish" : 0,
            "Vegetable" : 0,
            "Pescatarian" : 0,
            "Roasted" : 0,
            "Salad" : 0
        },
        "weapons": {
            "Wood Sword": {
                "quantity": 0,
                "durability": 5,
                "equipped": 0
            },
            "Sword": {
                "quantity": 0,
                "durability": 9,
                "equipped": 0
            },
            "Wood Shield": {
                "quantity": 0,
                "durability": 5,
                "equipped": 0
            },
            "Shield":{
                "quantity": 0,
                "durability": 9,
                "equipped": 0
            }
        }
    }

def collect_data(id):
    global data
    data = {
         "character" : {
            "game_id" : id,
            "user_name" : db.user_name(id),
            "position" : maps.player_position(id), 
            "hearts_remaining" : db.actual_hearts(id),
            "max_hearts" : db.max_hearts(id),
            "region" : db.region(id),
            "blood_moon_countdown" : db.blood_moon_countdown(id)
        },
        "foods" : {
            "Meat" : db.food_totals(id)["Meat"],
            "Fish" : db.food_totals(id)["Fish"],
            "Vegetable" : db.food_totals(id)["Vegetable"],
            "Pescatarian" : db.food_totals(id)["Pescatarian"],
            "Roasted" : db.food_totals(id)["Roasted"],
            "Salad" : db.food_totals(id)["Salad"]
        },
        "weapons": {
            "Wood Sword": {
                "quantity": db.weapon_quantity(id)["Wood Sword"],
                "durability": db.weapon_durability(id)["Wood Sword"],
                "equipped": db.is_equipped(id, "Wood Sword")
            },
            "Sword": {
                "quantity": db.weapon_quantity(id)["Sword"],
                "durability": db.weapon_durability(id)["Sword"],
                "equipped": db.is_equipped(id, "Sword")
            },
            "Wood Shield": {
                "quantity": db.weapon_quantity(id)["Wood Shield"],
                "durability": db.weapon_durability(id)["Wood Shield"],
                "equipped": db.is_equipped(id, "Wood Shield")
            },
            "Shield":{
                "quantity": db.weapon_quantity(id)["Shield"],
                "durability": db.weapon_durability(id)["Shield"],
                "equipped": db.is_equipped(id, "Shield")
            }
        }
    }


def is_equipped(weapon):
    if(data["weapons"][weapon]["equipped"]==1):
        return "(equipped)"
    else:
        return " "
    
def weapons_equipped():
    equipped = []
    for weapon in ["Sword","Wood Sword","Shield","Wood Shield"]:
        if(data["weapons"][weapon]["equipped"]==1):
            equipped.append(weapon)
    if(len(equipped)==0):
        return ["",""]
    elif(len(equipped)==1):
        return equipped+[""]
    return equipped

def total_food():
    total = 0
    for food in data["foods"]:
        total += data["foods"][food]
    return total

def total_weapons():
    total = 0
    for weapon in data["weapons"]:
        total += data["weapons"][weapon]["quantity"]
    return total    
