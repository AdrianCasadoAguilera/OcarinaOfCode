import maps, math, data


def go_by(tipo, region):
    lista = []
    for i in range(len(maps.maps[region])):
        for j in range(len(maps.maps[region][i])):
            if maps.maps[region][i][j] == tipo:
                lista.append([i,j])

    posicion = [11,7]

    distancias = []
    for k in lista:
        distancias.append(math.sqrt((k[0]- posicion[0])**2+(k[1]- posicion[1])**2))

    minimo = min(distancias)

    posiciones = [[0,1], [1,0], [1,1], [1,-1], [-1,-1], [0,-1], [-1,0], [-1, 1]]

    posiciones_validas = []
    for i in posiciones:
        if maps.maps[region][lista[distancias.index(minimo)][0]+i[0]][lista[distancias.index(minimo)][1]+i[1]] == " ":
            posiciones_validas.append([lista[distancias.index(minimo)][0]+i[0], lista[distancias.index(minimo)][1]+i[1]])

    distancias_validas = []
    for i in posiciones_validas:
        distancias_validas.append(math.sqrt((i[0]- posicion[0])**2+(i[1]- posicion[1])**2))

    posicion = posiciones_validas[distancias_validas.index(min(distancias_validas))]

    data.data["character"]["position"] = posicion