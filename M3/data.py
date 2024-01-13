import db

data = {}

locations = {
    "Hyrule":   {
            "enemies" : {
                1 : [1,[20,8]],
                2 : [9,[25,4]]
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
                "equipped": db.equipped(id, "Wood Sword")
            },
            "Sword": {
                "quantity": db.weapon_quantity(id)["Sword"],
                "durability": db.weapon_durability(id)["Sword"],
                "equipped": db.equipped(id, "Sword")
            },
            "Wood Shield": {
                "quantity": db.weapon_quantity(id)["Wood Shield"],
                "durability": db.weapon_durability(id)["Wood Shield"],
                "equipped": db.equipped(id, "Wood Shield")
            },
            "Shield":{
                "quantity": db.weapon_quantity(id)["Shield"],
                "durability": db.weapon_durability(id)["Shield"],
                "equipped": db.equipped(id, "Shield")
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

