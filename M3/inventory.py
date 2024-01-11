import db

# AUXULIAR FUNCTIONS

def total_food(id):
    dic = db.food_totals(id)
    total = 0
    for el in dic.values():
        total += el
    return str(total)

def total_weapons(id):
    dic = db.weapon_quantity(id)
    total = 0
    for el in dic.values():
        total += el
    return str(total)

# FUNCTIONS

def show_inventory(id,to_show):
    main = ["                ",
            db.name(id)+f"♥ {db.actual_hearts(id)}/{db.max_hearts(id)}".rjust(17-len(db.name(id))),
            "                ",
            "Equipment",
            db.weapons_equiped(id)[0].rjust(17),
            db.weapons_equiped(id)[1].rjust(17),
            " "*17,
            "Food"+total_food(id).rjust(13),
            "Weapons"+total_weapons(id).rjust(10),
            " "*17]
    
    weapons = [" "*17,
               " "*17,
               "Wood Sword"+(str(db.weapon_durability(id)["Wood Sword"])+"/"+str(db.weapon_quantity(id)["Wood Sword"])).rjust(17-len("Wood Sword")),
               "  " + db.equipped(id,"Wood Sword"),
               "Sword"+(str(db.weapon_durability(id)["Sword"])+"/"+str(db.weapon_quantity(id)["Sword"])).rjust(17-len("Sword")),
               "  " + db.equipped(id,"Sword"),
               "Wood Shield"+(str(db.weapon_durability(id)["Wood Shield"])+"/"+str(db.weapon_quantity(id)["Wood Shield"])).rjust(17-len("Wood Shield")),
               "  " + db.equipped(id,"Wood Shield"),
               "Shield"+(str(db.weapon_durability(id)["Shield"])+"/"+str(db.weapon_quantity(id)["Shield"])).rjust(17-len("Shield")),
               "  " + db.equipped(id,"Shield")]
    food = [" "*17,
            " "*17,
            "Vegetables"+str(db.food_totals(id)["Vegetable"]).rjust(7),
            "Fish"+str(db.food_totals(id)["Fish"]).rjust(13),
            "Meat"+str(db.food_totals(id)["Meat"]).rjust(13),
            " "*17,
            "Salads"+str(db.food_totals(id)["Salad"]).rjust(11),
            "Pescatarian"+str(db.food_totals(id)["Pescatarian"]).rjust(6),
            "Roasted"+str(db.food_totals(id)["Roasted"]).rjust(10),
            " "*17]
    
    if(to_show=="Main"):
        return main
    elif(to_show=="Weapons"):
        return weapons
    elif(to_show=="Food"):
        return food
    else:
        return []
