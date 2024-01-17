import maps, math
lista = []
mapa = "Hyrule"
tipo = "~"
for i in range(len(maps.maps[mapa])):
    for j in range(len(maps.maps[mapa][i])):
        if maps.maps[mapa][i][j] == tipo:
            lista.append([i,j])

posicion = [11,7]

distancias = []
for k in lista:
    distancias.append(math.sqrt((k[0]- posicion[0])**2+(k[1]- posicion[1])**2))

minimo = min(distancias)
print(lista[distancias.index(minimo)])

posiciones = [[0,1], [1,0], [1,1], [1,-1], [-1,-1], [0,-1], [-1,0], [-1, 1]]

posiciones_validas = []
for i in posiciones:
    if maps.maps[mapa][lista[distancias.index(minimo)][0]+i[0]][lista[distancias.index(minimo)][1]+i[1]] == " ":
        posiciones_validas.append([lista[distancias.index(minimo)][0]+i[0], lista[distancias.index(minimo)][1]+i[1]])

for i in posiciones_validas:
    print(i)

for i in posiciones_validas:
    print(maps.maps[mapa][i[0]][i[1]])

distancias_validas = []
for i in posiciones_validas:
    distancias_validas.append(math.sqrt((i[0]- posicion[0])**2+(i[1]- posicion[1])**2))

for i in range(len(posiciones_validas)):
    print(posiciones_validas[i], distancias_validas[i])

print(posiciones_validas[distancias_validas.index(min(distancias_validas))])

posicion = posiciones_validas[distancias_validas.index(min(distancias_validas))]

print(posicion)