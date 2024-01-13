import data

# FUNCTIONS

def show_inventory(id,to_show):
    main = ["                ",
            data.data["character"]["user_name"]+f"♥ {data.data['character']['hearts_remaining']}/{data.data['character']['max_hearts']}".rjust(17-len(data.data["character"]["user_name"])),
            "                ",
            "Equipment",
            data.weapons_equipped()[0].rjust(17),
            data.weapons_equipped()[1].rjust(17),
            " "*17,
            "Food"+str(data.total_food()).rjust(13),
            "Weapons"+str(data.total_weapons()).rjust(10),
            " "*17]
    
    weapons = [" "*17,
               " "*17,
               "Wood Sword"+(str(data.data["weapons"]["Wood Sword"]["durability"])+"/"+str(data.data["weapons"]["Wood Sword"]["quantity"])).rjust(17-len("Wood Sword")),
               "  " + data.is_equipped("Wood Sword"),
               "Sword"+(str(data.data["weapons"]["Sword"]["durability"])+"/"+str(data.data["weapons"]["Sword"]["quantity"])).rjust(17-len("Sword")),
               "  " + data.is_equipped("Sword"),
               "Wood Shield"+(str(data.data["weapons"]["Wood Shield"]["durability"])+"/"+str(data.data["weapons"]["Wood Shield"]["quantity"])).rjust(17-len("Wood Shield")),
               "  " + data.is_equipped("Wood Shield"),
               "Shield"+(str(data.data["weapons"]["Shield"]["durability"])+"/"+str(data.data["weapons"]["Shield"]["quantity"])).rjust(17-len("Shield")),
               "  " + data.is_equipped("Shield")]
    food = [" "*17,
            " "*17,
            "Vegetables"+str(data.data["foods"]["Vegetable"]).rjust(7),
            "Fish"+str(data.data["foods"]["Fish"]).rjust(13),
            "Meat"+str(data.data["foods"]["Meat"]).rjust(13),
            " "*17,
            "Salads"+str(data.data["foods"]["Salad"]).rjust(11),
            "Pescatarian"+str(data.data["foods"]["Pescatarian"]).rjust(6),
            "Roasted"+str(data.data["foods"]["Roasted"]).rjust(10),
            " "*17]
    
    if(to_show=="Main"):
        return main
    elif(to_show=="Weapons"):
        return weapons
    elif(to_show=="Food"):
        return food
    else:
        return []
