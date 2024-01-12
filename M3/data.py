import db
# Working on this dictionary

data = {}

def initialize_data(id):
    global data
    data = {
         "character" : {
            "game_id" : id,
            "user_name" : db.user_name(id),
            "position" : [], ############################################## HAY QUE CAMBIAR LA POSICIÓN INICIAL POR UNA FUNCION QUE DEVUELVA LA LISTA BUSCANDO EN EL MAPA EL ! 
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
                "lifes_remaining": db.weapon_durability(id)["Wood Sword"],
                "equipped": db.equiped(id, "Wood Sword")
            },
            "Sword": {
                "quantity": db.weapon_quantity(id)["Sword"],
                "durability": db.weapon_durability(id)["Sword"],
                "equipped": db.equiped(id, "Sword")
            },
            "Wood Shield": {
                "quantity": db.weapon_quantity(id)["Wood Shield"],
                "lifes_remaining": db.weapon_durability(id)["Wood Shield"],
                "equipped": db.equiped(id, "Wood Shield")
            },
            "Shield":{
                "quantity": db.weapon_quantity(id)["Shield"],
                "lifes_remaining": db.weapon_durability(id)["Shield"],
                "equipped": db.equiped(id, "Shield")
            }
        }
    }