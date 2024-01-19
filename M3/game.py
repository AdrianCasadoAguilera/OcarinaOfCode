import screen as scr,maps,inventory as inv,db,random,data,math

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
    
    data.data["character"]["blood_moon_countdown"] -= 1

    if data.data["character"]["blood_moon_countdown"] == 0:
        blood_moon()

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

def where_is_enemy():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "E"):
            return [pos_x+1,pos_y]
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "E"):
                return [pos_x,pos_y+1]
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "E"):
                    return [pos_x+1,pos_y+1]
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "E"):
                        return [pos_x-1,pos_y]
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "E"):
                            return [pos_x,pos_y-1]
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "E"):
                                return [pos_x-1,pos_y-1]
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "E"):
                                    return [pos_x+1,pos_y-1]
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "E"):
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

def where_is_sanctuary():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "S"):
            return [pos_x+1,pos_y]
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "S"):
                return [pos_x,pos_y+1]
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "S"):
                    return [pos_x+1,pos_y+1]
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "S"):
                        return [pos_x-1,pos_y]
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "S"):
                            return [pos_x,pos_y-1]
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "S"):
                                return [pos_x-1,pos_y-1]
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "S"):
                                    return [pos_x+1,pos_y-1]
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "S"):
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
    region = data.data["character"]["region"]
    enemy_pos = where_is_enemy()
    for key,value in data.locations[region]["enemies"].items():
        if(value[1]==enemy_pos):
            index = key
            break
    data.locations[region]["enemies"][index][0] -= 1
    scr.add_to_prompt(f'Brave, keep fighting, {data.data["character"]["user_name"]}')
    protect = use_shield()
    if(data.locations[region]["enemies"][index][0] > 0 and protect==False):
        data.data["character"]["hearts_remaining"] -= 1
    elif(protect==True):
        scr.add_to_prompt("Enemy has hit the shield! You don't recieve damage.")
    if(data.data["character"]["hearts_remaining"]>0):
        scr.add_to_prompt(f"Be careful {data.data['character']['user_name']}! You only have {data.data['character']['hearts_remaining']} hearts!")
    directions = ["up", "down", "left", "right"]
    x, y = data.locations[region]["enemies"][index][1][0], data.locations[region]["enemies"][index][1][1]
    if data.locations[region]["enemies"][index][0] == 0:
        maps.maps[region][x][y] = " "
    while(True):
        direction = random.randint(0,3)
        if directions[direction] == "up":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][0] -= 1
                maps.maps[region][x][y], maps.maps[region][x-1][y] = maps.maps[region][x-1][y], maps.maps[region][x][y]
                break
        elif directions[direction] == "down":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][0] += 1
                maps.maps[region][x][y], maps.maps[region][x+1][y] = maps.maps[region][x+1][y], maps.maps[region][x][y]
                break
        elif directions[direction] == "left":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][1] -= 1
                maps.maps[region][x][y], maps.maps[region][x][y-1] = maps.maps[region][x][y-1], maps.maps[region][x][y]
                break
        elif directions[direction] == "right":
            if check_enemy_movement(directions[direction], index, region):
                data.locations[region]["enemies"][index][1][1] += 1
                maps.maps[region][x][y], maps.maps[region][x][y+1] = maps.maps[region][x][y+1], maps.maps[region][x][y]
                break
    data.data["weapons"][weapon]["durability"] -= 1
    if not shield == " ":
        data.data["weapons"][shield]["durability"] -= 1

    if data.locations[region]["enemies"][index][0] == 0:
        maps.maps[region][x][y] = " "

def attack_fox():
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

    region = data.data["character"]["region"]
    data.locations[region]["fox"][0] -= 1
    loc_fox_x = int(data.locations[data.data["character"]["region"]]["fox"][1][0])
    loc_fox_y = int(data.locations[data.data["character"]["region"]]["fox"][1][1])    
    if data.locations[region]["fox"][0] == 0:
        maps.maps[region][loc_fox_x][loc_fox_y] = " "
    data.data["weapons"][weapon]["durability"] -= 1
    if not shield == " ":
        data.data["weapons"][shield]["durability"] -= 1
    add_food("Meat",1)
    scr.add_to_prompt("You got meat")
    data.locations[region]["fox"][0] = 1

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

def open_sanctuary():
    loc = where_is_sanctuary()
    region = data.data["character"]["region"]
    for key,sanct in data.locations[region]["sanctuaries"].items():
        if(sanct[1]==loc and data.locations[region]["sanctuaries"][key][0]==1):
                data.locations[region]["sanctuaries"][key][0] -= 1
                data.data["character"]["max_hearts"] += 1
                data.data["character"]["hearts_remaining"] = data.data["character"]["max_hearts"]
                db.update_database(data.data)


def who_attacks():
    pos_x, pos_y = data.data["character"]["position"][1], data.data["character"]["position"][0]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]

    # Definir direcciones relativas para buscar alrededor del personaje
    directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    dic = {"E": "enemy", "F": "fox", "T": "tree"}
    for dir_x, dir_y in directions:
        for tipo in ["E", "F", "T"]:
            try:
                target = region_map[pos_y + dir_y][pos_x + dir_x]
                if target == tipo:
                    return dic[tipo]
            except IndexError:
                pass

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

def can_open():
    pos_x = data.data["character"]["position"][0]
    pos_y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    region_map = maps.maps[region]
    try:
        if(region_map[pos_x+1][pos_y] == "M" or region_map[pos_x+1][pos_y] == "S"):
            return True
    except:
        pass
    finally:
        try:
            if(region_map[pos_x][pos_y+1] == "M" or region_map[pos_x][pos_y+1] == "S"):
                return True
        except:
            pass
        finally:
            try:
                if(region_map[pos_x+1][pos_y+1] == "M" or region_map[pos_x+1][pos_y+1] == "S"):
                    return True
            except:
                pass
            finally:
                try:
                    if(region_map[pos_x-1][pos_y] == "M" or region_map[pos_x-1][pos_y] == "S"):
                        return True
                except:
                    pass
                finally:
                    try:
                        if(region_map[pos_x][pos_y-1] == "M" or region_map[pos_x][pos_y-1] == "S"):
                            return True
                    except:
                        pass
                    finally:
                        try:
                            if(region_map[pos_x-1][pos_y-1] == "M" or region_map[pos_x-1][pos_y-1] == "S"):
                                return True
                        except:
                            pass
                        finally:
                            try:
                                if(region_map[pos_x+1][pos_y-1] == "M" or region_map[pos_x+1][pos_y-1] == "S"):
                                    return True
                            except:
                                pass
                            finally:
                                try:
                                    if(region_map[pos_x-1][pos_y+1] == "M" or region_map[pos_x-1][pos_y+1] == "S"):
                                        return True
                                except:
                                    return False
    return False

def add_weapon(weapon):
    global data
    data.data["weapons"][weapon]["quantity"] += 1
    db.update_database(data.data)

def remove_food(food,quantity):
    global data
    if data.data["foods"][food] >= quantity:
        data.data["foods"][food] -= quantity

def add_food(food,quantity):
    global data
    data.data["foods"][food] += quantity
    db.update_database(data.data)

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
    elif(food=="Roasted"):
        increase_health(4)
    else:
        scr.add_to_prompt(f"You cannot eat {food}!")
        
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
    if(act_location==selected_map):
        raise ValueError(f"You are allready there")
    elif(act_location=="Hyrule" and (selected_map=="Gerudo" or selected_map=="Death Mountain")):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        prob_fox_appear()
        db.update_database(data.data)
    elif(act_location=="Death Mountain" and (selected_map=="Hyrule" or selected_map=="Necluda")):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        prob_fox_appear()
        db.update_database(data.data)
    elif(act_location=="Gerudo" and (selected_map=="Hyrule" or selected_map=="Necluda")):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        prob_fox_appear()
        db.update_database(data.data)
    elif(act_location=="Necluda" and (selected_map=="Death Mountain" or selected_map=="Gerudo")):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        prob_fox_appear()
        db.update_database(data.data)
    elif(selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        db.change_map(act_location, id)
    elif(act_location=="Castle"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        data.data["character"]["position"] = maps.player_position(id)
        db.update_database(data.data)
    else:
        raise ValueError(f"You can't go to {selected_map} from here")
    
def equip(weapon):
    if(data.data["weapons"][weapon]["quantity"]>0 and data.data["weapons"][weapon]["equipped"]==0):
        for el in data.weapons_equipped():
            if(el == weapon):
                raise ValueError(f"You alredy have {el} equipped!")
            if(len(el)>0):
                if(el.split()[-1] == weapon.split()[-1]):
                    raise ValueError(f"You alredy have a {el.split()[-1]} equipped!")
        data.data["weapons"][weapon]["equipped"] = 1
        scr.add_to_prompt(f"{weapon} equipped")
    elif(data.data["weapons"][weapon]["quantity"]==0):
        raise ValueError(f"You don't have {weapon}")

def unequip(weapon):
    if(data.data["weapons"][weapon]["equipped"]==1):
        for el in data.weapons_equipped():
            if(el == weapon):
                data.data["weapons"][weapon]["equipped"] = 0
                scr.add_to_prompt(f"{weapon} unequipped")
    elif(data.data["weapons"][weapon]["quantity"]==0):
        raise ValueError(f"You don't have {weapon}")
    else:
        raise ValueError(f"You alredy have {weapon} unequipped!")
    
def use_shield():
    prob_deflect = random.randint(1,10)
    if data.is_equipped("Wood Shield") == "(equipped)":
        if prob_deflect <=2:
            return True
        else:
            return False
    elif data.is_equipped("Shield") == "(equipped)":
        if prob_deflect <=3:
            return True
        else: 
            return False
    return False

def prob_fox_appear():
    prob_fox = random.randint(0,1)
    loc_fox_x = int(data.locations[data.data["character"]["region"]]["fox"][1][0])
    loc_fox_y = int(data.locations[data.data["character"]["region"]]["fox"][1][1])
    region = data.data["character"]["region"]
    if (prob_fox==0):
        maps.maps[region][loc_fox_x][loc_fox_y] = "F"
        scr.add_to_prompt("You see a Fox")
    elif (prob_fox==1):
        maps.maps[region][loc_fox_x][loc_fox_y] = " "
        scr.add_to_prompt("You don't see a Fox")

# CHEAT FUNCTIONS

def cheat_rename(new_name):
    global data
    try:
        if check_name(new_name):
            data.data["character"]["user_name"] = new_name
            scr.add_to_prompt(f"Cheating: rename player to {new_name}")
        else:
            raise TypeError
    except TypeError:
        print("The new name is not valid")

def cheat_add(option):
    global data
    food = ["Meat","Fish","Vegetable"]
    try:
        if option in data.data["weapons"]:
            data.data["weapons"][option]["quantity"] += 1
            scr.add_to_prompt(f"Cheating: add {option.lower()}")
            db.update_database(data.data)
        elif option in food:
            data.data["foods"][option] += 1
            scr.add_to_prompt(f"Cheating: add {option.lower()}")
            db.update_database(data.data)
        else:
            raise TypeError
    except TypeError:
        scr.add_to_prompt("Add a valid optionnn")

def cheat_cook_food(food):
    global data
    try:
        if food == "Salad":
            data.data["food"]["Vegetable"] += 2
            cook(food)
        elif food == "Pescatarian":
            data.data["food"]["Fish"] += 1
            data.data["food"]["Vegetable"] += 1
            cook(food)
            db.update_database(data.data)
        elif food == "Roasted":
            data.data["food"]["Meat"] += 1
            data.data["food"]["Vegetable"] += 1
            cook(food)
            db.update_database(data.data)
        else:
            raise TypeError
        scr.add_to_prompt(f"Cheating: cook {food.lower()}")
    except TypeError:
        scr.add_to_prompt("Add a valid option")


def cheat_open_sanctuaries():
    global locations, data
    for map in ["Hyrule","Gerudo","Necluda","Death Mountain"]:
            for sanct in data.locations[map]["sanctuaries"].keys():
                data.locations[map]["sanctuaries"][sanct][0] = 0     ############# actualizar cuando se tenga hecho locations definitivo
    data.data["character"]["max_hearts"] = 9
    data.data["character"]["hearts_remaining"] = data.data["character"]["max_hearts"]
    scr.add_to_prompt("Cheating: open sanctuaries")

def cheat_game_over():
    global data
    data.data["character"]["hearts_remaining"] = 0
    scr.add_to_prompt("Cheating: game over")

def cheat_win_game():
    global ganons_life
    ganons_life = -1
    scr.add_to_prompt("Cheating: win game")
    zelda_saved()

def check_name(name):
   if(len(name)<3 or len(name)>10):
      scr.add_to_prompt(f"'{name}' is not a valid name")
      return False
   else:
      for i in range(len(name)):
         if(not(name[i].isalnum())):
            scr.add_to_prompt(f"'{name}' is not a valid name")
            return False
      return True

# MAIN FUNCTIONS

def link_death():
    global data
    while True:
        titol_seccio = "Link's death"
        options = ["Continue"]
        lines = """



        Game Over.





    """.split("\n")
        scr.add_to_prompt("Nice try, you died. Game is over.")
        scr.print_menu_screen(lines,options,titol_seccio)
        x = input("What to do now? ")
        if(x.capitalize()==options[0]):
            data.data["character"]["hearts_remaining"] = data.data["character"]["max_hearts"]
            break
        scr.add_to_prompt("Invalid Action")

def check_enemy_movement(direction, enemy_index, region):
    y, x = data.locations[region]["enemies"][enemy_index][1][0], data.locations[region]["enemies"][enemy_index][1][1]
    try:
        if direction == "up":
            if maps.maps[region][y-1][x] == " " and [y-1, x] != data.data["character"]["position"]:
                return True
        elif direction == "down":
            if maps.maps[region][y+1][x] == " " and [y+1, x] != data.data["character"]["position"]:
                return True
        elif direction == "left":
            if maps.maps[region][y][x-1] == " " and [y, x-1] != data.data["character"]["position"]:
                return True
        elif direction == "right":
            if maps.maps[region][y][x+1] == " " and [y, x+1] != data.data["character"]["position"]:
                return True
    except:
        return False
    return False

def blood_moon():
    global data, locations, maps

    for region in maps.maps.keys():
        for i in range(len(maps.maps[region])):
            for j in range(len(maps.maps[region][i])):
                if maps.maps[region][i][j] == "E":
                    maps.maps[region][i][j] = " "

    data.locations["Hyrule"]["enemies"] = {
            1 : [1,[8,20]],
            2 : [9,[4,35]]
        }
    data.locations["Gerudo"]["enemies"] = {
            1: [1, [3, 2]],
            2: [2, [5, 37]]
        }
    data.locations["Death Mountain"]["enemies"] = {
            1 : [2,[4,13]],
            2 : [2,[3,51]]
        }
    data.locations["Necluda"]["enemies"] = {
            1 : [1,[2,10]],
            2 : [2,[6,38]]
        }
    
    for region in data.locations.keys():
        for value in data.locations[region]["enemies"].values():
            maps.maps[region][value[1][0]][value[1][1]] = "E"

    data.data["character"]["blood_moon_countdown"] = 25

    scr.add_to_prompt(f"The Blood moon rises once again. Please be careful, {data.data['character']['user_name']}.")

    db.cur.execute(f"UPDATE game SET blood_moon_appearances = blood_moon_appearances + 1 WHERE game_id = {data.data['character']['game_id']}")


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
          ['limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', 'limit', '|', ' ', '|', ' ', '|', '|', ' ', ' ', '_', ' ', ' ', '|', '|', ' ', '|', ' ', '|', " ", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', 'O', 'T', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', '|', '#', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', " ", ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
          [' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
        if(x.capitalize()==options[0]):
            data.data["character"]["hearts_remaining"] = 9
            data.data["character"]["max_hearts"] = 9
            break
        scr.add_to_prompt("Invalid Action")

def play(id,act_location):
    global ganons_life
    inv_title = "Main"
    data.collect_data(id)
    prob_fox_appear()
    while True:
        try:
            # CHECK ELEMENTS
            update_ganons_hearts()

            pos = data.data["character"]["position"]
            for weapon in data.data["weapons"]:
                if(data.data["weapons"][weapon]["durability"]==0):
                    data.data["weapons"][weapon]["quantity"]-=1
                    db.cur.execute(f"UPDATE weapons_used SET quantity_used = quantity_used + 1 WHERE game_id = {data.data['characters']['game_id']} and weapon_name = {weapon}")
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
            if(can_open()==False):
                options.remove("Open")
            act_location = data.data["character"]["region"]
            if(act_location=="Castle"):
                options = ["Back","Go","Attack","Eat","Show","Equip","Unequip"]
            mat = maps.maps[act_location]
            inventory = inv.show_inventory(inv_title)
            scr.print_screen(pos,options,mat,inventory,inv_title,act_location)
            x = input("What to do now? ").split()
            if(len(x)==0):
                raise ValueError("Invalid Action")
            elif(x[0].lower()=="cheat" and len(x) >= 3):
                if(x[1].lower() == "add"):
                    if len(x)==3:
                        cheat_add(x[2].capitalize())
                    elif len(x)==4:
                        option = x[2].capitalize()+" "+x[3].capitalize()
                        cheat_add(option)
                    else:
                        raise ValueError("Invalid Action")
                elif(x[1].lower()=="cook" and len(x)==3):
                    cheat_cook_food(x[2])
                elif(x[1].lower()=="open" and x[2].lower()=="sanctuaries" and len(x)==3):
                    cheat_open_sanctuaries()
                elif(x[1].lower()=="game" and x[2].lower()=="over" and len(x)==3):
                    cheat_game_over()
                elif(x[1].lower()=="win" and x[2].lower()=="game" and len(x)==3):   
                    cheat_win_game() 
                elif(len(x)==4):
                    if((x[1].lower()+" "+x[2].lower()+" "+x[3].lower())=="rename player to"):
                        cheat_rename(x[4])
                    else:
                        raise ValueError("Invalid Action")
                else:
                    raise ValueError("Write a valid option")
            elif(x[0].capitalize() not in options):
                raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Exit" and len(x)==1):
                break
            elif(x[0].capitalize()=="Show" and len(x)==2):
                if x[1].capitalize()=="Map":
                    show_map(inventory, inv_title)
                else:
                    raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Show" and len(x)==3):
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
                    raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Eat" and len(x)==2):
                if(x[1].lower() in ["vegetable","salad","pescatarian","roasted"]):
                    if(data.data["foods"][x[1].capitalize()]>0 and data.data["character"]["hearts_remaining"]<data.data["character"]["max_hearts"]):
                        eat(x[1].capitalize())
                    elif(data.data["character"]["hearts_remaining"]==data.data["character"]["max_hearts"]):
                        scr.add_to_prompt(f"You alredy have {db.max_hearts(id)} hearts!")
                    else:
                        scr.add_to_prompt(f"Not enough {x[1].capitalize()}")
                else:
                    raise ValueError("Invalid Action")
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
                    if(x[1].capitalize() == "By" and x[2].capitalize() == "The" and ((x[3].upper() in ["T", "WATER", "F", "C", "M", "E", "W", "O"] or (len(x[3]) == 2 and x[3][0].upper() == "S" and x[3][1] in ('0','1','2','3','4','5','6'))))):
                        if x[3].upper() == "WATER":
                            go_by("~", data.data["character"]["region"])
                        elif(x[3][0].upper() == "S"):
                            go_by_sanct(int(x[3][1]), data.data["character"]["region"])
                        else:
                            go_by(x[3].upper(), data.data["character"]["region"])
                    else:
                        raise ValueError("Invalid Action")
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
                elif(objective=="fox"):
                    attack_fox()
            elif(x[0].lower()=="equip" and len(x)>2 and len(x)<5):
                if(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                else:
                    x[2] = x[2].capitalize()
                if(x[1].lower() == "the" and x[2].lower() in ["sword","shield","wood sword","wood shield"]):
                    equip(x[2])
                else:
                    raise ValueError("Invalid Action")
            elif(x[0].lower()=="unequip" and len(x)>2 and len(x)<5):
                if(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                else:
                    x[2] = x[2].capitalize()
                if(x[1].lower() == "the" and x[2].lower() in ["sword","shield","wood sword","wood shield"]):
                    unequip(x[2])
                else:
                    raise ValueError("Invalid Action")
            elif(x[0].lower()=="fish" and len(x)==1):
                fishing()
            elif(x[0].lower()=="open" and x[1].lower()=="chest" and len(x)==2):
                open_chest()
            elif(x[0].lower()=="open" and x[1].lower()=="sanctuary"):
                open_sanctuary()
            elif(x[0].lower()=="back"):
                if(data.data["character"]["region"]=="Castle"):
                    ganons_life = 8
                comp_map(act_location,last_location,id)
            else:
                raise ValueError("Invalid Action")
        except ValueError as e:
            scr.add_to_prompt(e)
        else:
            pass_turn()

def go_by(tipo, region):
    lista = []
    for i in range(len(maps.maps[region])):
        for j in range(len(maps.maps[region][i])):
            if maps.maps[region][i][j] == tipo:
                lista.append([i,j])

    posicion = data.data["character"]["position"]

    distancias = []
    for k in lista:
        distancias.append(math.sqrt((k[0]- posicion[0])**2+(k[1]- posicion[1])**2))
    if(len(distancias)>0):
        minimo = min(distancias)
    else:
        raise ValueError("Invalid Action")

    posiciones = [[0,1], [1,0], [1,1], [1,-1], [-1,-1], [0,-1], [-1,0], [-1, 1]]

    posiciones_validas = []
    for i in posiciones:
        try:
            if maps.maps[region][lista[distancias.index(minimo)][0]+i[0]][lista[distancias.index(minimo)][1]+i[1]] == " ":
                posiciones_validas.append([lista[distancias.index(minimo)][0]+i[0], lista[distancias.index(minimo)][1]+i[1]])
        except:
            pass
        

    distancias_validas = []
    for i in posiciones_validas:
        distancias_validas.append(math.sqrt((i[0]- posicion[0])**2+(i[1]- posicion[1])**2))

    posicion = posiciones_validas[distancias_validas.index(min(distancias_validas))]

    data.data["character"]["position"] = posicion
    

def go_by_sanct(sanctuary_number, region):
    posicion = data.data["character"]["position"]
    position_sanctuary = 0
    for key in data.locations[region]["sanctuaries"].keys():
        if key == sanctuary_number:
            position_sanctuary = data.locations[region]["sanctuaries"][sanctuary_number][1]
    if(position_sanctuary == 0):
        raise ValueError("Invalid Action")
    
    posiciones = [[0,1], [1,0], [1,1], [1,-1], [-1,-1], [0,-1], [-1,0], [-1, 1]]

    posiciones_validas = []
    
    for i in posiciones:
        try:
            if maps.maps[region][position_sanctuary[0]+i[0]][position_sanctuary[1]+i[1]] == " ":
                posiciones_validas.append([position_sanctuary[0]+i[0], position_sanctuary[1]+i[1]])
        except:
            pass
    distancias_validas = []
    for i in posiciones_validas:
        distancias_validas.append(math.sqrt((i[0]- posicion[0])**2+(i[1]- posicion[1])**2))

    posicion = posiciones_validas[distancias_validas.index(min(distancias_validas))]

    data.data["character"]["position"] = posicion