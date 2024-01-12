import data

# AUXULIAR FUNCTIONS

def total_food(id):
    dic = data.food_totals(id)
    total = 0
    for el in dic.values():
        total += el
    return str(total)

# FUNCTIONS

def show_inventory(id,to_show):
    main = ["                ",
            data.name(id)+f"♥ {data.actual_hearts(id)}/{data.max_hearts(id)}".rjust(17-len(data.name(id))),
            "                ",
            "Equipment",
            data.weapons_equiped(id)[0].rjust(17),
            data.weapons_equiped(id)[1].rjust(17),
            " "*17,
            "Food"+total_food(16).rjust(13),
            " "*17,
            " "*17]
    
    weapons = [" "*17,
               " "*17,
               "Wood Sword"+str(data.weapon_durability(id)["Wood Sword"])+"/"+str(data.weapon_quantity(id)["Wood Sword"]).rjust(len("Wood Sword")-17),
               "  " + data.equipped(id,"Wood Sword"),
               "Sword"+str(data.weapon_durability(id)["Sword"])+"/"+str(data.weapon_quantity(id)["Sword"]).rjust(len("Sword")-17),
               "  " + data.equipped(id,"Sword"),
               "Wood Shield"+str(data.weapon_durability(id)["Wood Shield"])+"/"+str(data.weapon_quantity(id)["Wood Shield"]).rjust(len("Wood Shield")-17),
               "  " + data.equipped(id,"Wood Shield"),
               "Shield"+str(data.weapon_durability(id)["Shield"])+"/"+str(data.weapon_quantity(id)["Shield"]).rjust(len("Shield")-17),
               "  " + data.equipped(id,"Shield"),
               ]
    food = [" "*17,
            " "*17,
            "Vegetables"+str(data.food_totals(id)["Vegetables"]).rjust(7),
            "Fish"+str(data.food_totals(id)["Fish"]).rjust(13),
            "Meat"+str(data.food_totals(id)["Meat"]).rjust(13),
            " "*17,
            "Salads"+str(data.food_totals(id)["Salads"]).rjust(11),
            "Pescatarian"+str(data.food_totals(id)["Pescatarian"]).rjust(6),
            "Roasted"+str(data.food_totals(id)["Roasted"]).rjust(10),
            " "*17]
    
    if(to_show=="Inventory"):
        return main
    elif(to_show=="Weapons"):
        return weapons
    elif(to_show=="Food"):
        return food
    else:
        return []
    