import screen as scr, maps, data

def play(id):
    scr.print_screen()

def can_open_chest(pos,map_name):
    pos_x = pos[0]
    pos_y = pos[1]
    loc = maps.maps[map_name]
    try:
        if(loc[pos_x+1][pos_y]=="M" or loc[pos_x][pos_y+1]=="M" or loc[pos_x-1][pos_y]=="M" or loc[pos_x][pos_y-1]=="M" or loc[pos_x+1][pos_y+1]=="M" or loc[pos_x+1][pos_y-1]=="M" or loc[pos_x-1][pos_y-1]=="M" or loc[pos_x-1][pos_y+1]=="M"):
            return True
        return False
    except:
        return False
    
def add_weapon(weapon):
    global data
    data["weapon"][weapon]["quantity"] += 1

def chest(map_name):
    if map_name == "Hyrule" or map_name == "Gerudo":
        add_weapon("Sword")
    elif map_name == "Death Mountain" or map_name == "Necluda":
        add_weapon("Shield")