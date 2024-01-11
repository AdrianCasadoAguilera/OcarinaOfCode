import screen as scr,maps,inventory as inv,db

pos = [1,16]

# AUXILIAR FUNCTIONS

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
    loc = maps.locations[map_name]
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

def play(id,act_location):
    inv_title = "Main"
    while True:
        try:
            options = ["Exit","Attack","Go","Unequip","Eat","Cook","Fish","Open","Show"]
            if(can_cook(pos,"Hyrule")==False):
                options.remove("Cook")
            mat = maps.locations[act_location]
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

        except ValueError as e:
            scr.add_to_prompt(e)