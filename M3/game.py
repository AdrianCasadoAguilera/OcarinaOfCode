import screen as scr,maps,inventory as inv

def play(id,act_location):
    while True:
        try:
            options = ["Exit","Attack","Go","Unequip","Eat","Cook","Fish","Open"]
            mat = maps.locations[act_location]
            inv_title = "Inventory"
            inventory = inv.show_inventory(id,inv_title)
            scr.print_screen(options,mat,inventory,inv_title,act_location)
            x = input("What to do now? ").split()
            if(x[0].capitalize() not in options):
                raise ValueError("Invalid Action")
            elif(x[0].capitalize()=="Exit" and len(x)==1):
                break
        except ValueError as e:
            scr.add_to_prompt(e)