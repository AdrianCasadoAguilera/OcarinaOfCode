import screen as scr,maps,inventory as inv,db

# AUXILIAR FUNCTIONS

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
    if(loc[pos_x+1][pos_y]=="C" or loc[pos_x][pos_y+1]=="C" or loc[pos_x-1][pos_y]=="C" or loc[pos_x][pos_y-1]=="C" or loc[pos_x+1][pos_y+1]=="C" or loc[pos_x+1][pos_y-1]=="C" or loc[pos_x-1][pos_y-1]=="C" or loc[pos_x-1][pos_y+1]=="C"):
        return True
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
        else:
            scr.add_to_prompt("Not enough Vegetable")
    elif(food=="Pescatarian"):
        if(db.food_totals(id)["Vegetable"]>=1 and db.food_totals(id)["Fish"]>=1):
            remove_food(id,"Fish",1)
            remove_food(id,"Vegetable",1)
            add_food(id,"Pescatarian",1)
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
        elif(db.food_totals(id)["Vegetable"]<1):
            scr.add_to_prompt("Not enough Vegetable")
        elif(db.food_totals(id)["Meat"]<1):
            scr.add_to_prompt("Not enough Meat")
        else:
            scr.add_to_prompt("Not enough Meat and Vegetable")
# MAIN FUNCTIONS

def play(id,act_location):
    inv_title = "Main"
    while True:
        try:
            pos = [1,16]
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
            

        except ValueError as e:
            scr.add_to_prompt(e)