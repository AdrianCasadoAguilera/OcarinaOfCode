import db

# AUXULIAR FUNCTIONS

def total_food(id):
    dic = db.food_totals(id)
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
            "Food"+total_food(16).rjust(13),
            " "*17,
            " "*17]
    
    weapons = []
    food = [" "*17,
            " "*17,
            "Vegetables"+str(db.food_totals(id)["Vegetables"]).rjust(7),
            "Fish"+str(db.food_totals(id)["Fish"]).rjust(13),
            "Meat"+str(db.food_totals(id)["Meat"]).rjust(13),
            " "*17,
            "Salads"+str(db.food_totals(id)["Salads"]).rjust(11),
            "Pescatarian"+str(db.food_totals(id)["Pescatarian"]).rjust(6),
            "Roasted"+str(db.food_totals(id)["Roasted"]).rjust(10),
            " "*17]
    
    if(to_show=="Inventory"):
        return main
    elif(to_show=="Weapons"):
        return weapons
    elif(to_show=="Food"):
        return food
    else:
        return []
    
# print(show_inventory(16))