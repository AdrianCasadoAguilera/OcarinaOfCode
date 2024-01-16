import screen as scr,maps,inventory as inv,db,random,data,game_functions

# GANON'S LIFE
ganons_life = 8

# AUXILIAR FUNCTIONS

def pass_turn():
    region = data.data["character"]["region"]
    for key in data.locations[region]["trees"].keys():
        if(data.locations[region]["trees"][key][0]<0):
            data.locations[region]["trees"][key][0]+=1
            if(data.locations[region]["trees"][key][0]>-3):
                maps.maps[region][data.locations[region]["trees"][key][1][0]][data.locations[region]["trees"][key][1][1]] = "t"
            elif(data.locations[region]["trees"][key][0]>-7):
                maps.maps[region][data.locations[region]["trees"][key][1][0]][data.locations[region]["trees"][key][1][1]] = "|"
            else:
                maps.maps[region][data.locations[region]["trees"][key][1][0]][data.locations[region]["trees"][key][1][1]] = "."
        if(data.locations[region]["trees"][key][0]==0):
            data.locations[region]["trees"][key][0]=4
            maps.maps[region][data.locations[region]["trees"][key][1][0]][data.locations[region]["trees"][key][1][1]] = "T"   

    #Option for opened chests 
    for key in data.locations[region]["chests"].keys():
        if(data.locations[region]["chests"][key][0]==0):
            maps.maps[region][data.locations[region]["chests"][key][1][0]][data.locations[region]["chests"][key][1][1]] = "W"
        else:
            maps.maps[region][data.locations[region]["chests"][key][1][0]][data.locations[region]["chests"][key][1][1]] = "M"

def attack_grass():
    if(data.data["character"]["region"]!="Castle"):
        prob = random.randint(1,10)
        if(data.data["weapons"]["Wood Sword"]["equipped"]==1 or data.data["weapons"]["Sword"]["equipped"]==1):
            if(prob==1):
                add_food("Meat",1)
                scr.add_to_prompt("You got a lizard!")

def where_is_tree():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "T"):
            return [pos_x+1,pos_y]
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "T"):
                return [pos_x,pos_y+1]
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "T"):
                    return [pos_x+1,pos_y+1]
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "T"):
                        return [pos_x-1,pos_y]
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "T"):
                            return [pos_x,pos_y-1]
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "T"):
                                return [pos_x-1,pos_y-1]
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "T"):
                                    return [pos_x+1,pos_y-1]
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "T"):
                                        return [pos_x-1,pos_y+1]
                                except:
                                    pass

def where_is_chest():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "M"):
            return [pos_x+1,pos_y]
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "M"):
                return [pos_x,pos_y+1]
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "M"):
                    return [pos_x+1,pos_y+1]
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "M"):
                        return [pos_x-1,pos_y]
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "M"):
                            return [pos_x,pos_y-1]
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "M"):
                                return [pos_x-1,pos_y-1]
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "M"):
                                    return [pos_x+1,pos_y-1]
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "M"):
                                        return [pos_x-1,pos_y+1]
                                except:
                                    pass
    
def attack_tree():
    prob = random.randint(1,10)
    ws_equipped = data.is_equipped("Wood Sword")
    s_equipped = data.is_equipped("Sword")
    if(ws_equipped=="(equipped)"):
        equipped = "Wood Sword"
    elif(s_equipped=="(equipped)"):
        equipped = "Sword"
    else:
        equipped = " "
    if(equipped=="Wood Sword" or equipped=="Sword"):
        data.data["weapons"][equipped]["durability"] -= 1
        loc = where_is_tree()
        region = data.data["character"]["region"]
        for key,tree in data.locations[region]["trees"].items():
            if(tree[1]==loc):
                 data.locations[region]["trees"][key][0] -= 1
            if(data.locations[region]["trees"][key][0] == 0):
                data.locations[region]["trees"][key][0] = -10
        if(prob<=4):
            add_food("Vegetable",1)
            scr.add_to_prompt("You got an apple!")
        elif(prob<=6):
            add_weapon("Wood Sword")
            scr.add_to_prompt("You got a Wooden Sword!")
        elif(prob<=8):
            add_weapon("Wood Shield")
            scr.add_to_prompt("You got a Wooden Shield!")
    else:
        if(prob<=4):
            add_food("Vegetable",1)
            scr.add_to_prompt("You got an apple!")
        elif(prob<=5):
            weapon_prob = random.randint(0,1)
            if(weapon_prob==0):
                add_weapon("Wood Sword")
                scr.add_to_prompt("You got a Wooden Sword!")
            else:
                add_weapon("Wood Shield")
                scr.add_to_prompt("You got a Wooden Shield!")


def attack_enemy():
    global maps, locations

    if data.is_equipped("Wood Sword") == "(equipped)":
        weapon = "Wood Sword"
    elif data.is_equipped("Sword") == "(equipped)":
        weapon = "Sword"
    else:
        scr.add_to_prompt("You need to equip a sword to attack an enemy!")
        return

    if data.is_equipped("Wood Shield") == "(equipped)":
        shield = "Wood Shield"
    elif data.is_equipped("Shield") == "(equipped)":
        shield = "Shield"
    elif data.is_equipped("Shield") == " " and data.is_equipped("Wood Shield") == " ":
        shield = " "

    index = game_functions.search_nearest("E")
    region = data.data["character"]["region"]
    data.locations[region]["enemies"][index][0] -= 1
    directions = ["up", "down", "left", "right"]
    x, y = data.locations[region]["enemies"][index][1][0], data.locations[region]["enemies"][index][1][1]
    if data.locations[region]["enemies"][index][0] == 0:
        maps.maps[region][y][x] = " "
    while(True):
        direction = random.randint(0,3)
        if directions[direction] == "up":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][1] -= 1
                maps.maps[region][y][x], maps.maps[region][y-1][x] = maps.maps[region][y-1][x], maps.maps[region][y][x]
                break
        elif directions[direction] == "down":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][1] += 1
                maps.maps[region][y][x], maps.maps[region][y+1][x] = maps.maps[region][y+1][x], maps.maps[region][y][x]
                break
        elif directions[direction] == "left":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][0] -= 1
                maps.maps[region][y][x], maps.maps[region][y][x-1] = maps.maps[region][y][x-1], maps.maps[region][y][x]
                break
        elif directions[direction] == "right":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][0] += 1
                maps.maps[region][y][x], maps.maps[region][y][x+1] = maps.maps[region][y][x+1], maps.maps[region][y][x]
                break
    data.data["weapons"][weapon]["durability"] -= 1
    if not shield == " ":
        data.data["weapons"][shield]["durability"] -= 1

    if data.locations[region]["enemies"][index][0] == 0:
        maps.maps[region][y][x] = " "

def fishing():
    prob = random.randint(1,10)
    region = data.data["character"]["region"]
    if data.locations[region]["fishing"] != 0:
        if prob <= 2:
            add_food("Fish",1)
            data.locations[region]["fishing"] = 0
            scr.add_to_prompt("You got a fish")
        elif prob > 2:
            scr.add_to_prompt("You didn't get a fish")
    else:
        scr.add_to_prompt("You can't fish right now")        

def open_chest():
    region = data.data["character"]["region"]
    if region == "Hyrule" or region == "Gerudo":
        scr.add_to_prompt("You got a Sword") 
        add_weapon("Sword")
    elif region == "Death" or region == "Necluda":
        scr.add_to_prompt("You got a Shield")
        add_weapon("Shield")
    loc = where_is_chest()
    for key,chest in data.locations[data.data["character"]["region"]]["chests"].items():
        if(chest[1]==loc):
                data.locations[data.data["character"]["region"]]["chests"][key][0] -= 1
    for key in data.locations.keys():
        for value in data.locations[key]["chests"].values():
            if value[0]==1:
                return
    for key in data.locations.keys():
        for value in data.locations[key]["chests"].values():
                value[0] = 1


def who_attacks():
    x = data.data["character"]["position"][1]
    y = data.data["character"]["position"][0]
    region = data.data["character"]["region"]
    mapa = maps.maps
    try:
        if mapa[region][y-1][x] == "E" or mapa[region][y+1][x] == "E" or mapa[region][y][x+1] == "E" or mapa[region][y][x-1] == "E" or mapa[region][y-1][x-1] == "E" or mapa[region][y-1][x+1] == "E" or mapa[region][y+1][x-1] == "E" or mapa[region][y+1][x+1] == "E":
            return "enemy"
    except:
        print()
    finally:
        try:
            if mapa[region][y-1][x] == "F" or mapa[region][y+1][x] == "F" or mapa[region][y][x+1] == "F" or mapa[region][y][x-1] == "F" or mapa[region][y-1][x-1] == "F" or mapa[region][y-1][x+1] == "F" or mapa[region][y+1][x-1] == "F" or mapa[region][y+1][x+1] == "F":
                return "fox"
        except:
            print()
        finally:
            try:
                if mapa[region][y-1][x] == "T" or mapa[region][y+1][x] == "T" or mapa[region][y][x+1] == "T" or mapa[region][y][x-1] == "T" or mapa[region][y-1][x-1] == "T" or mapa[region][y-1][x+1] == "T" or mapa[region][y+1][x-1] == "T" or mapa[region][y+1][x+1] == "T":
                    return "tree"
            except:
                print()   
    return "grass"

def check_movement(direction):
    global data
    x = data.data["character"]["position"][0]
    y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    
    if direction == "left":
        try:
            if maps.maps[region][x][y-1] == " " or maps.maps[region][x][y-1] == "!":
                if y-1 < 0:
                    return False
                data.data["character"]["position"][1] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "right":
        try:
            if maps.maps[region][x][y+1] == " " or maps.maps[region][x][y+1] == "!":
                if y+1 < 0:
                    return False
                data.data["character"]["position"][1] += 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "up":
        try:
            if maps.maps[region][x-1][y] == " " or  maps.maps[region][x-1][y] == "!":
                if x-1 < 0:
                    return False
                data.data["character"]["position"][0] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "down":
        try:
            if maps.maps[region][x+1][y] == " " or maps.maps[region][x+1][y] == "!":
                if x+1 < 0:
                    return False
                data.data["character"]["position"][0] += 1
                return True
            else:
                return False
        except:
            return False

def inventory_help():
    while True:
        try:
            options = ["Back"]
            titol_seccio = "Help, inventory"
            lines = """       
            Type 'show inventory main' to show the main inventory
                    (main, weapons, Food)
            Type 'eat X' to eat X, where X is a Food item
            Type 'Cook X' to Cook X, where X is a Food item
            Type 'equip X' to equip X, where X is a weapon
            Type 'unequip X' to unequip X, where X is a weapon
            Type 'back' now to go back to the 'Game'
            
            """.split("\n")
            scr.print_menu_screen(lines,options,titol_seccio)
            x = input("What to do now? ")
            if(x.capitalize() == "Back"):
                return
            raise ValueError("Invalid Action")
        except ValueError as e:
            scr.add_to_prompt(e)

def can_cook():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "C"):
            return True
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "C"):
                return True
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "C"):
                    return True
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "C"):
                        return True
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "C"):
                            return True
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "C"):
                                return True
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "C"):
                                    return True
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "C"):
                                        return True
                                except:
                                    return False
    return False

def can_fish():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "~"):
            return True
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "~"):
                return True
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "~"):
                    return True
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "~"):
                        return True
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "~"):
                            return True
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "~"):
                                return True
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "~"):
                                    return True
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "~"):
                                        return True
                                except:
                                    return False
    return False

def can_chest():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "M"):
            return True
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "M"):
                return True
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "M"):
                    return True
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "M"):
                        return True
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "M"):
                            return True
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "M"):
                                return True
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "M"):
                                    return True
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "M"):
                                        return True
                                except:
                                    return False
    return False

def add_weapon(weapon):
    global data
    data.data["weapons"][weapon]["quantity"] += 1

def remove_food(food,quantity):
    global data
    if data.data["foods"][food] >= quantity:
        data.data["foods"][food] -= quantity

def add_food(food,quantity):
    global data
    data.data["foods"][food] += quantity

def cook(food):
    if(food == "Salad"):
        if(data.data["foods"]["Vegetable"]>=2):
            remove_food("Vegetable",2)
            add_food("Salad",1)
            scr.add_to_prompt("Cooked Salad.")
        else:
            scr.add_to_prompt("Not enough Vegetable")
    elif(food=="Pescatarian"):
        if(data.data["foods"]["Vegetable"]>=1 and data.data["foods"]["Fish"]>=1):
            remove_food("Fish",1)
            remove_food("Vegetable",1)
            add_food("Pescatarian",1)
            scr.add_to_prompt("Cooked Pescatarian.")
        elif(data.data["foods"]["Vegetable"]<1):
            scr.add_to_prompt("Not enough Vegetable")
        elif(data.data["foods"]["Fish"]<1):
            scr.add_to_prompt("Not enough Fish")
        else:
            scr.add_to_prompt("Not enough Fish and Vegetable")
    elif(food=="Roasted"):
        if(data.data["foods"]["Vegetable"]>=1 and data.data["foods"]["Meat"]>=1):
            remove_food("Meat",1)
            remove_food("Vegetable",1)
            add_food("Roasted",1)
            scr.add_to_prompt("Cooked Roasted.")
        elif(data.data["foods"]["Vegetable"]<1):
            scr.add_to_prompt("Not enough Vegetable")
        elif(data.data["foods"]["Meat"]<1):
            scr.add_to_prompt("Not enough Meat")
        else:
            scr.add_to_prompt("Not enough Meat and Vegetable")

def increase_health(quantity):
    global data
    data.data["character"]["hearts_remaining"] += quantity
    if(data.data["character"]["hearts_remaining"]>data.data["character"]["max_hearts"]):
        data.data["character"]["hearts_remaining"] = data.data["character"]["max_hearts"]

def eat(food):
    remove_food(food,1)
    if(food=="Vegetable"):
        increase_health(1)
    elif(food=="Salad"):
        increase_health(2)
    elif(food=="Pescatarian"):
        increase_health(3)
    else:
        increase_health(4)
        
def show_map(inventory, inv_title):
    mat = maps.maps["General Map"]
    while True:
        scr.print_screen([-1,-1],"Back ",mat,inventory,inv_title,"General Map")
        x = input("What to do now? ")    
        if(x.capitalize()=="Back"):
            break
        else:
             scr.add_to_prompt("Invalid Action")
        
def map_position(selected_map):
    if(selected_map=="Gerudo"):
        data.data["character"]["position"] = [2,9]
    elif(selected_map=="Hyrule"):
        data.data["character"]["position"] = [11,8]
    elif(selected_map=="Death Mountain"):
        data.data["character"]["position"] = [2,9]
    elif(selected_map=="Necluda"):
        data.data["character"]["position"] = [2,2]
    elif(selected_map=="Castle"):
        data.data["character"]["position"] = [4,9]

def comp_map(act_location,selected_map,id):
    global data
    selected_map = selected_map
    if(act_location=="Hyrule" and selected_map=="Gerudo" or selected_map=="Death Mountain"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
    elif(act_location=="Death Mountain" and selected_map=="Hyrule" or selected_map=="Necluda"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
    elif(act_location=="Gerudo" and selected_map=="Hyrule" or selected_map=="Necluda"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
    elif(act_location=="Necluda" and selected_map=="Death Mountain" or selected_map=="Gerudo"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
    elif(selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        db.change_map(act_location, id)
    elif(act_location=="Castle"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
    else:
        raise ValueError(f"You can't go to {selected_map} from here")
def equip(weapon):
    if(data.data["weapons"][weapon]["quantity"]>0 and data.data["weapons"][weapon]["equipped"]==0):
        for el in data.weapons_equipped():
            if(el == weapon):
                raise ValueError(f"You alredy have {el} equipped!")
        data.data["weapons"][weapon]["equipped"] = 1
    elif(data.data["weapons"][weapon]["quantity"]==0):
        raise ValueError(f"You don't have {weapon}")

def unequip(weapon):
    if(data.data["weapons"][weapon]["equipped"]==1):
        for el in data.weapons_equipped():
            if(el == weapon):
                data.data["weapons"][weapon]["equipped"] = 0
    elif(data.data["weapons"][weapon]["quantity"]==0):
        raise ValueError(f"You don't have {weapon}")
    else:
        raise ValueError(f"You alredy have {weapon} unequipped!")
    
def shield(id):
    prob_deflect = random.randint(1,10)
    if db.is_equipped(id,"Wood Shield") == 1:
        if prob_deflect <=2:
            return True
        else:
            return False
    elif db.is_equipped(id,"Shield") == 1:
        if prob_deflect <=3:
            return True
        else: 
            return False

# MAIN FUNCTIONS

def link_death():
    global data
    while True:
        titol_seccio = "Link's death"
        options = ["Continue"]
        lines = """



        Game Over.





    """.split("\n")
        scr.print_menu_screen(lines,options,titol_seccio)
        scr.add_to_prompt("Nice try, you died. Game is over.")
        x = input("What to do now? ")
        if(x.capitalize()==options[0]):
            data.data["character"]["hearts_remaining"] = data.data["character"]["max_hearts"]
            break
        scr.add_to_prompt("Invalid Action")

def play(id,act_location):
    global ganons_life
    inv_title = "Main"
    data.collect_data(id)
    while True:
        try:
            # CHECK ELEMENTS
            pass_turn()
            update_ganons_hearts()
            pos = data.data["character"]["position"]
            for weapon in data.data["weapons"]:
                if(data.data["weapons"][weapon]["durability"]==0):
                    data.data["weapons"][weapon]["quantity"]-=1
                    if(data.data["weapons"][weapon]["quantity"]==0):
                        data.data["weapons"][weapon]["equipped"] = 0
                    if(weapon.split(" ")[0] == "Wood"):
                        data.data["weapons"][weapon]["durability"]=5
                    else:
                        data.data["weapons"][weapon]["durability"]=9
            
            options = ["Exit","Attack","Go","Equip","Unequip","Eat","Cook","Fish","Open","Show"]
            if(data.data["character"]["hearts_remaining"]<=0):
                link_death()
                break
            if(can_cook()==False):
                options.remove("Cook")
            if(can_fish()==False):
                options.remove("Fish")
            if(can_chest()==False):
                options.remove("Open")
            act_location = data.data["character"]["region"]
            if(act_location=="Castle"):
                options = ["Back","Go","Attack","Eat","Show","Equip","Unequip"]
            mat = maps.maps[act_location]
            inventory = inv.show_inventory(id,inv_title)
            scr.print_screen(pos,options,mat,inventory,inv_title,act_location)
            x = input("What to do now? ").split()
            if(len(x)==0):
                raise ValueError("Invalid Action")
            if(x[0].capitalize() not in options):
                raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Exit" and len(x)==1):
                break
            elif(x[0].capitalize()=="Show" and len(x)==2):
                if x[1].capitalize()=="Map":
                    show_map(inventory, inv_title)
                else:
                    raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Show" and len(x)==3):
                print(x[1],x[2])
                if(x[1].capitalize()=="Inventory" and x[2].lower() in ["main","food","weapons"]):
                    inv_title = x[2].capitalize()
                elif(x[1].capitalize()=="Inventory" and x[2].lower()=="help"):
                    inventory_help()
                else: 
                    raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Cook" and len(x)==2):
                if(x[1].capitalize() in ["Salad","Pescatarian","Roasted"]):
                    cook(x[1].capitalize())
                else:
                    scr.add_to_prompt("Invalid Action")
            elif(x[0].capitalize()=="Eat" and len(x)==2):
                if(x[1].lower() in ["vegetable","fish","meat","salad","pescatarian","roasted"]):
                    if(data.data["foods"][x[1].capitalize()]>0 and data.data["character"]["hearts_remaining"]<data.data["character"]["max_hearts"]):
                        eat(x[1].capitalize())
                    elif(data.data["character"]["hearts_remaining"]==data.data["character"]["max_hearts"]):
                        scr.add_to_prompt(f"You alredy have {db.max_hearts(id)} hearts!")
                    else:
                        scr.add_to_prompt(f"Not enough {x[1].capitalize()}")
                else:
                    scr.add_to_prompt("Invalid Action")
            elif(x[0].capitalize()=="Go"):
                if(len(x)==3):
                    if(x[1].lower() in ["up","down","left","right"] and x[2].isdigit()):
                        movements = int(x[2])
                        while movements>0:
                            valid = check_movement(x[1].lower())
                            movements -= 1
                            if(not valid):
                                scr.add_to_prompt("You can't go there, it's not a valid position!")
                                break
                        if(data.data["character"]["region"]=="Castle"):
                            pos = data.data["character"]["position"][1]
                            if(pos>=18 and ganons_life>0):
                                data.data["character"]["hearts_remaining"] -= 1
                    elif(x[1].capitalize()== "To" and x[2].capitalize() in maps.maps.keys()):
                        if(x[2].capitalize()=="Castle"):
                            last_location = act_location
                        comp_map(act_location, x[2].capitalize(),id)
                elif(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                    if(x[1].lower()=="to" and x[2] == "Death Mountain"):
                        comp_map(act_location, x[2],id)
            elif(x[0].lower()=="attack" and len(x)==1):
                if(act_location=="Castle" and who_attacks()!="tree"):
                    pos = data.data["character"]["position"][1]
                    if(pos>=18 and data.is_equipped("Wood Sword")=="(equipped)" or data.is_equipped("Sword")=="(equipped)"):
                        ganon()
                    elif pos<18:
                        raise ValueError("You need to get closer to Ganon.")
                    else:
                        raise ValueError("You need a sword to fight against Ganon.")
                objective = who_attacks()
                if(objective=="grass"):
                    attack_grass()
                elif(objective=="tree"):
                    attack_tree()
                elif(objective=="enemy"):
                    attack_enemy()
            elif(x[0].lower()=="equip" and len(x)>2 and len(x)<5):
                if(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                else:
                    x[2] = x[2].capitalize()
                if(x[1].lower() == "the" and x[2].lower() in ["sword","shield","wood sword","wood shield"]):
                    equip(x[2])
            elif(x[0].lower()=="unequip" and len(x)>2 and len(x)<5):
                if(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                else:
                    x[2] = x[2].capitalize()
                if(x[1].lower() == "the" and x[2].lower() in ["sword","shield","wood sword","wood shield"]):
                    unequip(x[2])
            elif(x[0].lower()=="fish" and len(x)==1):
                fishing()
            elif(x[0].lower()=="open" and x[1].lower()=="chest" and len(x)==2):
                open_chest()
            elif(x[0].lower()=="back"):
                if(data.data["character"]["region"]=="Castle"):
                    ganons_life = 8
                comp_map(act_location,last_location,id)
        except ValueError as e:
            scr.add_to_prompt(e)

def check_enemy_movement(direction, enemy_index, region):
    x, y = data.locations[region]["enemies"][enemy_index][1][0], data.locations[region]["enemies"][enemy_index][1][1]
    try:
        if direction == "up":
            if maps.maps[region][y-1][x] == " " and [x, y-1] != data.data["character"]["position"]:
                return True
        elif direction == "down":
            if maps.maps[region][y+1][x] == " " and [x, y+1] != data.data["character"]["position"]:
                return True
        elif direction == "left":
            if maps.maps[region][y][x-1] == " " and [x-1, y] != data.data["character"]["position"]:
                return True
        elif direction == "right":
            if maps.maps[region][y][x+1] == " " and [x+1, y] != data.data["character"]["position"]:
                return True
    except:
        return False
    return False

def blood_moon():
    global data
            


def ganon():
    global ganons_life
    ganons_life -= 1
    if(ganons_life>0):
        data.data["character"]["hearts_remaining"] -= 1
    elif(ganons_life==0):
        zelda_saved()
        ganons_life = -1


def update_ganons_hearts():
    if(ganons_life == 8):
        maps.maps["Castle"][1][54] = "♥"
        maps.maps["Castle"][1][53] = "♥"
        maps.maps["Castle"][1][52] = "♥"
        maps.maps["Castle"][1][51] = "♥"
        maps.maps["Castle"][1][50] = "♥"
        maps.maps["Castle"][1][49] = "♥"
        maps.maps["Castle"][1][48] = "♥"
        maps.maps["Castle"][1][47] = "♥"
    if ganons_life <= 7:
        maps.maps["Castle"][1][54] = " "
    if ganons_life <= 6:
        maps.maps["Castle"][1][53] = " "
    if ganons_life <= 5:
        maps.maps["Castle"][1][52] = " "
    if ganons_life <= 4:
        maps.maps["Castle"][1][51] = " "
    if ganons_life <= 3:
        maps.maps["Castle"][1][50] = " "
    if ganons_life <= 2:
        maps.maps["Castle"][1][49] = " "
    if ganons_life <= 1:
        maps.maps["Castle"][1][48] = " "
    if ganons_life <= 0:
        maps.maps["Castle"][1][47] = " "

def zelda_saved():
    global data
    while True:
        titol_seccio = "Zelda saved"
        options = ["Continue"]
        lines = """



        Congratulations, Link has saved Princess Zelda.
        Thanks for playing!




    """.split("\n")
        scr.print_menu_screen(lines,options,titol_seccio)
        scr.add_to_prompt("You saved Zelda, you won the game")
        x = input("What to do now? ")
        maps.maps["Castle"] = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', '-', '-', ' ', 'O', ' ', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '>', ' ', ' ', 'v', '-', 'v', '-', 'v', '-', 'v', ' ', ' ', ' ', '|', '>', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '_', '\\', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '/', '_', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", "'", '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', '|', ' ', ' ', '_', ' ', ' ', '|', '|', ' ', '|', ' ', '|', " ", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', 'O', 'T', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', '|', '#', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', " ", ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
        if(x.capitalize()==options[0]):
            data.data["character"]["hearts_remaining"] = 9
            data.data["character"]["max_hearts"] = 9
            break
        scr.add_to_prompt("Invalid Action")
