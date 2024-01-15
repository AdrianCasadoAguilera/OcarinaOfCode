import screen as scr,maps,inventory as inv,db,random,data

# AUXILIAR FUNCTIONS

def pass_turn():
    for key,value in data.locations[data.data["character"]["region"]]["trees"].items():
        if(data.locations[data.data["character"]["region"]]["trees"][key][0]<0):
            data.locations[data.data["character"]["region"]]["trees"][key][0]+=1
            if(data.locations[data.data["character"]["region"]]["trees"][key][0]>-3):
                maps.maps[data.data["character"]["region"]][data.locations[data.data["character"]["region"]]["trees"][key][1][0]][data.locations[data.data["character"]["region"]]["trees"][key][1][1]] = "t"
            elif(data.locations[data.data["character"]["region"]]["trees"][key][0]>-7):
                maps.maps[data.data["character"]["region"]][data.locations[data.data["character"]["region"]]["trees"][key][1][0]][data.locations[data.data["character"]["region"]]["trees"][key][1][1]] = "|"
            else:
                maps.maps[data.data["character"]["region"]][data.locations[data.data["character"]["region"]]["trees"][key][1][0]][data.locations[data.data["character"]["region"]]["trees"][key][1][1]] = "."
        if(data.locations[data.data["character"]["region"]]["trees"][key][0]==0):
            data.locations[data.data["character"]["region"]]["trees"][key][0]=4
            maps.maps[data.data["character"]["region"]][data.locations[data.data["character"]["region"]]["trees"][key][1][0]][data.locations[data.data["character"]["region"]]["trees"][key][1][1]] = "T"
        

def attack_grass():
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
        for key,tree in data.locations[data.data["character"]["region"]]["trees"].items():
            if(tree[1]==loc):
                 data.locations[data.data["character"]["region"]]["trees"][key][0] -= 1
            if(data.locations[data.data["character"]["region"]]["trees"][key][0] == 0):
                data.locations[data.data["character"]["region"]]["trees"][key][0] = -10
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
                data.data["character"]["position"][1] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "right":
        try:
            if maps.maps[region][x][y+1] == " " or maps.maps[region][x][y+1] == "!":
                data.data["character"]["position"][1] += 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "up":
        try:
            if maps.maps[region][x-1][y] == " " or  maps.maps[region][x-1][y] == "!":
                data.data["character"]["position"][0] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "down":
        try:
            if maps.maps[region][x+1][y] == " " or maps.maps[region][x+1][y] == "!":
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
    x = data.data["character"]["position"][0]
    y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    loc = maps.maps[region]
    try:
        if(loc[x+1][y]=="C" or loc[x][y+1]=="C" or loc[x-1][y]=="C" or loc[x][y-1]=="C" or loc[x+1][y+1]=="C" or loc[x+1][y-1]=="C" or loc[x-1][y-1]=="C" or loc[x-1][y+1]=="C"):
            return True
        return False
    except:
        return False
def can_fish():
    x = data.data["character"]["position"][0]
    y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    loc = maps.maps[region]
    try:
        if(loc[x+1][y]=="~" or loc[x][y+1]=="~" or loc[x-1][y]=="~" or loc[x][y-1]=="~" or loc[x+1][y+1]=="~" or loc[x+1][y-1]=="~" or loc[x-1][y-1]=="~" or loc[x-1][y+1]=="~"):
            return True
        return False
    except:
        return False

def can_fish():
    x = data.data["character"]["position"][0]
    y = data.data["character"]["position"][1]
    region = data.data["character"]["region"]
    loc = maps.maps[region]
    try:
        if(loc[x+1][y]=="~" or loc[x][y+1]=="~" or loc[x-1][y]=="~" or loc[x][y-1]=="~" or loc[x+1][y+1]=="~" or loc[x+1][y-1]=="~" or loc[x-1][y-1]=="~" or loc[x-1][y+1]=="~"):
            return True
        return False
    except:
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
    region = data.data["character"]["region"]
    data.locations[region]["fishing"] = 1
    mat = maps.maps["General Map"]
    scr.print_screen([-1,-1],"Back ",mat,inventory,inv_title,"General Map") #!!!!!!!!!!!!!!!!!!!! CAMBIAR POSICION PERSONAJE PARA QUE NO SALGA EN EL MAPA
    while True:
        x = input("What to do now? ")    
        if(x.capitalize()=="Back"):
            break
        else:
            raise ValueError("Invalid Action") #!!!!!!!!!!!!!!!!!!!! NEED FIX 
        
def map_position(selected_map):
    if(selected_map=="Gerudo"):
        data.data["character"]["position"] = [2,9]
    elif(selected_map=="Hyrule"):
        data.data["character"]["position"] = [11,8]
    elif(selected_map=="Death"):
        data.data["character"]["position"] = [2,9]
    elif(selected_map=="Necluda"):
        data.data["character"]["position"] = [2,2]
    elif(selected_map=="Castle"):
        data.data["character"]["position"] = [4,9]

def comp_map(act_location,selected_map,id):
    global data
    selected_map = selected_map.lower().capitalize()
    if(act_location=="Hyrule" and selected_map=="Gerudo" or selected_map=="Death" or selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        db.change_map(selected_map, id)
        maps.player_position(id)
    elif(act_location=="Death" and selected_map=="Hyrule" or selected_map=="Necluda" or selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        maps.player_position(id)
        db.change_map(selected_map, id)
    elif(act_location=="Gerudo" and selected_map=="Hyrule" or selected_map=="Necluda" or selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        maps.player_position(id)
        db.change_map(selected_map, id)
    elif(act_location=="Necluda" and selected_map=="Death" or selected_map=="Gerudo" or selected_map=="Castle"):
        data.data["character"]["region"] = selected_map
        maps.player_position(id)
        db.change_map(selected_map, id)
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
            data.data["character"]["hearts_remaining"] = 3
            break
        scr.add_to_prompt("Invalid Action")

def play(id,act_location):
    inv_title = "Main"
    data.collect_data(id)
    while True:
        try:
            # CHECK ELEMENTS
            pass_turn()
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
            if(data.data["character"]["hearts_remaining"]==0):
                link_death()
                break
            if(can_cook()==False):
                options.remove("Cook")
            if(can_fish()==False):
                options.remove("Fish")
            mat = maps.maps[data.data["character"]["region"]]
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
                    show_map(inventory, inv_title,id)
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
                if(x[1].lower() in ["vegetable","salad","pescatarian","roasted"]):
                    if(data.data["foods"][x[1].capitalize()]>0 and data.data["character"]["hearts_remaining"]<data.data["character"]["max_hearts"]):
                        eat(x[1].capitalize())
                    elif(data.data["character"]["hearts_remaining"]==data.data["character"]["max_hearts"]):
                        scr.add_to_prompt(f"You alredy have {db.max_hearts(id)} hearts!")
                    else:
                        scr.add_to_prompt(f"Not enough {x[1].capitalize()}")
                else:
                    scr.add_to_prompt("Invalid Action")
            elif(x[0].capitalize()=="Go" and len(x)==3):
                if(x[1].lower() in ["up","down","left","right"] and x[2].isdigit()):
                    movements = int(x[2])
                    while movements>0:
                        valid = check_movement(x[1].lower())
                        movements -= 1
                        if(not valid):
                            scr.add_to_prompt("You can't go there, it's not a valid position!")
                            break
                elif(x[0].capitalize()=="Go" and x[1].capitalize()== "To" and x[2].capitalize() in maps.maps.keys()):
                    comp_map(act_location, x[2],id)
            elif(x[0].lower()=="attack" and len(x)==1):
                objective = who_attacks()
                if(objective=="grass"):
                    attack_grass()
                elif(objective=="tree"):
                    attack_tree()
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


        except ValueError as e:
            scr.add_to_prompt(e)