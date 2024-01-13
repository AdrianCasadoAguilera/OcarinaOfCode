import math, maps, db

def search_position(tipo, id):
    lista = []
    region = db.region()
    mapa = maps.locations[region]
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == tipo:
                lista.append([x, y])
    return lista

def player_position(id):
    region = db.region()
    mapa = maps.locations[region]
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == "X":
                return x, y

def search_nearest(type):
    x, y = player_position()
    lista_objetos = search_position("T")
    minim = float('inf')
    index = -1
    for i in range(len(lista_objetos)):
        distancia = math.sqrt((lista_objetos[i][0] - x)**2 + (lista_objetos[i][1]- y)**2)
        if distancia < minim:
            minim = distancia
            index = i
    return minim, index

print(search_nearest("T"))

def check_movement(direction, positions, id):
    x, y = player_position()
    region = db.region(id)
    if direction == "left":
        try:
            if maps.locations[region][y][x-positions] == " ":
                return True
            else:
                return False
        except:
            return False
    elif direction == "right":
        try:
            if maps.location[region][y][x+positions] == " ":
                return True
            else:
                return False
        except:
            return False
    elif direction == "up":
        try:
            if maps.location[region][y-positions][x] == " ":
                return True
            else:
                return False
        except:
            return False
    elif direction == "down":
        try:
            if maps.locations[region][y+positions][x] == " ":
                return True
            else:
                return False
        except:
            return False



def can_fish(id):
    x, y = player_position()
    region = db.region(id)
    try:
        if maps.locations[region][y-1][x] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y][x+1] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y][x-1] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y-1][x-1] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y-1][x+1] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x-1] == "~":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x+1] == "~":
            return True
    except:
        pass
    return False

def can_cook(id):
    x, y = player_position()
    region = db.region(id)
    try:
        if maps.locations[region][y-1][x] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y][x+1] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y][x-1] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y-1][x-1] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y-1][x+1] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x-1] == "C":
            return True
    except:
        pass
    try:
        if maps.locations[region][y+1][x+1] == "C":
            return True
    except:
        pass
    return False

def who_attacks(id):
    x, y = player_position()
    region = db.region(id)
    mapa = maps.locations[region]
    try:
        if mapa[region][y-1][x] == "E" or mapa[region][y+1][x] == "E" or mapa[region][y][x+1] == "E" or mapa[region][y][x-1] == "E" or mapa[region][y-1][x-1] == "E" or mapa[region][y-1][x+1] == "E" or mapa[region][y+1][x-1] == "E" or mapa[region][y+1][x+1] == "E":
            return "enemy"
    except:
        print()
    try:
        if mapa[region][y-1][x] == "F" or mapa[region][y+1][x] == "F" or mapa[region][y][x+1] == "F" or mapa[region][y][x-1] == "F" or mapa[region][y-1][x-1] == "F" or mapa[region][y-1][x+1] == "F" or mapa[region][y+1][x-1] == "F" or mapa[region][y+1][x+1] == "F":
            return "fox"
    except:
        print()
    try:
        if mapa[region][y-1][x] == "T" or mapa[region][y+1][x] == "E" or mapa[region][y][x+1] == "E" or mapa[region][y][x-1] == "E" or mapa[region][y-1][x-1] == "E" or mapa[region][y-1][x+1] == "E" or mapa[region][y+1][x-1] == "E" or mapa[region][y+1][x+1] == "E":
            return "tree"
    except:
        print()   
    return "grass"