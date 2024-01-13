import screen as scr,maps,inventory as inv,db,random,data

pos = [1,16]

# AUXILIAR FUNCTIONS

def attack_grass(id):
    prob = random.randint(1,10)
    if(db.equipped(id,"Wood Sword")=="(equipped)" or db.equipped(id,"Sword")=="(equipped)"):
        if(prob==1):
            add_food(id,"Meat",1)
            scr.add_to_prompt("You got a lizard!")

def attack_tree(id):
    prob = random.randint(1,10)
    if(db.equipped(id,"Wood Sword")=="(equipped)" or db.equipped(id,"Sword")=="(equipped)"):
        if(prob<=4):
            add_food(id,"Vegetable",1)
            scr.add_to_prompt("You got an apple!")
        elif(prob<=6):
            if(db.weapon_quantity(id)["Wood Sword"]==0):
                db.cur.execute(f'INSERT INTO weapons VALUES ("Wood Sword",{id},0,5,1);')
            else:
                db.cur.execute(f'UPDATE weapons SET quantity=(quantity+1) WHERE weapon_name="Wood Sword" and game_id = {id};')
            db.cur.execute("commit")
            scr.add_to_prompt("You got a Wooden Sword!")
        elif(prob<=8):
            if(db.weapon_quantity(id)["Wood Shield"]==0):
                db.cur.execute(f'INSERT INTO weapons VALUES ("Wood Shield",{id},0,5,1);')
            else:
                db.cur.execute(f'UPDATE weapons SET quantity=(quantity+1) WHERE weapon_name="Wood Shield" and game_id = {id};')
            db.cur.execute("commit")
            scr.add_to_prompt("You got a Wooden Shield!")

def who_attacks(id):
    x = pos[1]
    y = pos[0]
    region = db.region(id)
    mapa = maps.locations
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

def check_movement(direction, id):
    global pos
    y = pos[0]
    x = pos[1]
    region = db.region(id)
    if direction == "left":
        try:
            if maps.locations[region][y][x-1] == " ":
                pos[1] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "right":
        try:
            if maps.locations[region][y][x+1] == " ":
                pos[1] += 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "up":
        try:
            if maps.locations[region][y-1][x] == " ":
                pos[0] -= 1
                return True
            else:
                return False
        except:
            return False
    elif direction == "down":
        try:
            if maps.locations[region][y+1][x] == " ":
                pos[0] += 1
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

def can_cook(pos,map_name):
    pos_x = pos[0]
    pos_y = pos[1]
    loc = maps.maps[map_name]
    try:
        if(loc[pos_x+1][pos_y]=="C" or loc[pos_x][pos_y+1]=="C" or loc[pos_x-1][pos_y]=="C" or loc[pos_x][pos_y-1]=="C" or loc[pos_x+1][pos_y+1]=="C" or loc[pos_x+1][pos_y-1]=="C" or loc[pos_x-1][pos_y-1]=="C" or loc[pos_x-1][pos_y+1]=="C"):
            return True
        return False
    except:
        return False

def remove_food(id,food,quantity):
    if(db.food_totals(id)[food]==quantity):
        db.cur.execute(f'DELETE FROM foods WHERE food_name="{food}";')
    else:
        db.cur.execute(f'UPDATE foods SET quantity=(quantity-{quantity}) WHERE food_name="{food}" and game_id = {id};')
    db.cur.execute("commit")

def add_food(id,food,quantity):
    if(db.food_totals(id)[food]==0):
        db.cur.execute(f'INSERT INTO foods VALUES ("{food}",{id},{quantity})')
    else:
        db.cur.execute(f'UPDATE foods SET quantity = (quantity+{quantity}) WHERE food_name="{food}" and game_id = {id};')
    db.cur.execute("commit")

def cook(id,food):
    if(food == "Salad"):
        if(db.food_totals(id)["Vegetable"]>=2):
            remove_food(id,"Vegetable",2)
            add_food(id,"Salad",1)
            scr.add_to_prompt("Cooked Salad.")
        else:
            scr.add_to_prompt("Not enough Vegetable")
    elif(food=="Pescatarian"):
        if(db.food_totals(id)["Vegetable"]>=1 and db.food_totals(id)["Fish"]>=1):
            remove_food(id,"Fish",1)
            remove_food(id,"Vegetable",1)
            add_food(id,"Pescatarian",1)
            scr.add_to_prompt("Cooked Pescatarian.")
        elif(db.food_totals(id)["Vegetable"]<1):
            scr.add_to_prompt("Not enough Vegetable")
        elif(db.food_totals(id)["Fish"]<1):
            scr.add_to_prompt("Not enough Fish")
        else:
            scr.add_to_prompt("Not enough Fish and Vegetable")
    elif(food=="Roasted"):
        if(db.food_totals(id)["Vegetable"]>=1 and db.food_totals(id)["Meat"]>=1):
            remove_food(id,"Meat",1)
            remove_food(id,"Vegetable",1)
            add_food(id,"Roasted",1)
            scr.add_to_prompt("Cooked Roasted.")
        elif(db.food_totals(id)["Vegetable"]<1):
            scr.add_to_prompt("Not enough Vegetable")
        elif(db.food_totals(id)["Meat"]<1):
            scr.add_to_prompt("Not enough Meat")
        else:
            scr.add_to_prompt("Not enough Meat and Vegetable")

def increase_health(id,quantity):
    db.cur.execute(f"UPDATE game SET hearts_remaining = (hearts_remaining+{quantity}) WHERE game_id={id};")
    db.cur.execute("commit")
    if(db.actual_hearts(id)>db.max_hearts(id)):
        db.cur.execute(f"UPDATE game SET hearts_remaining = max_hearts WHERE game_id={id};")
        db.cur.execute("commit")

def eat(id,food):
    remove_food(id,food,1)
    if(food=="Vegetable"):
        increase_health(id,1)
    elif(food=="Salad"):
        increase_health(id,2)
    elif(food=="Pescatarian"):
        increase_health(id,3)
    else:
        increase_health(id,4)
        

# MAIN FUNCTIONS

def link_death(id):
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
            db.cur.execute(f"UPDATE game SET hearts_remaining=3 WHERE game_id={id};")
            db.cur.execute("commit")
            break
        scr.add_to_prompt("Invalid Action")

def play(id,act_location):
    inv_title = "Main"
    data.collect_data(id)
    while True:
        try:
            options = ["Exit","Attack","Go","Equip","Unequip","Eat","Cook","Fish","Open","Show"]
            if(db.actual_hearts(id)==0):
                link_death(id)
                break
            if(can_cook(pos,"Hyrule")==False):
                options.remove("Cook")
            mat = maps.maps[act_location]
            inventory = inv.show_inventory(id,inv_title)
            scr.print_screen(pos,options,mat,inventory,inv_title,act_location)
            x = input("What to do now? ").split()
            if(x[0].capitalize() not in options):
                raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Exit" and len(x)==1):
                break
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
                    cook(id,x[1].capitalize())
                else:
                    scr.add_to_prompt("Invalid Action")
            elif(x[0].capitalize()=="Eat" and len(x)==2):
                if(x[1].lower() in ["vegetable","salad","pescatarian","roasted"]):
                    if(db.food_totals(id)[x[1].capitalize()]>0 and db.actual_hearts(id)<db.max_hearts(id)):
                        eat(id,x[1].capitalize())
                    elif(db.actual_hearts(id)==db.max_hearts(id)):
                        scr.add_to_prompt(f"You alredy have {db.max_hearts(id)} hearts!")
                    else:
                        scr.add_to_prompt(f"Not enough {x[1].capitalize()}")
                else:
                    scr.add_to_prompt("Invalid Action")
            elif(x[0].capitalize()=="Go" and len(x)==3):
                if(x[1].lower() in ["up","down","left","right"] and x[2].isdigit()):
                    movements = int(x[2])
                    while movements>0:
                        valid = check_movement(x[1].lower(),id)
                        movements -= 1
                        if(not valid):
                            scr.add_to_prompt("You can't go there, it's not a valid position!")
                            break
            elif(x[0].lower()=="attack" and len(x)==1):
                objective = who_attacks(id)
                if(objective=="grass"):
                    attack_grass(id)
                elif(objective=="tree"):
                    attack_tree(id)
            elif(x[0].lower()=="equip" and len(x)>2 and len(x)<5):
                if(len(x)==4):
                    x[2] = x[2].capitalize() + " " + x[3].capitalize()
                else:
                    x[2] = x[2].capitalize()
                if(x[1].lower() == "the" and x[2].lower() in ["sword","shield","wood sword","wood shield"]):
                    print(x[2])
                    print(db.equipped(id,x[2]))
                    input()
                    if(db.weapon_quantity(id)[x[2]]>0 and db.equipped(id,x[2])==" "):
                        db.cur.execute(f'UPDATE weapons SET equipped = 1 WHERE game_id = {id} and weapon_name = "{x[2].capitalize()}"')
                    elif(db.equipped(id,[x[2]]=="(equipped)")):
                        raise ValueError(f"You alredy have {x[2]} equipped!")
                    else:
                        raise ValueError(f"You don't have {x[2]}!")


        except ValueError as e:
            scr.add_to_prompt(e)