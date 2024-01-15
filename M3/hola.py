import data

print("hOla".capitalize())

for key in data.locations.keys():
    for value in data.locations[key]["chests"].values():
        print(value[0])