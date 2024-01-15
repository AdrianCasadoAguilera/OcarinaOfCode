import data, menu, game, screen
def rename():
    global data
    try:
        new_name = input("What's your new name?")
        if menu.check_name(new_name):
            data.data["character"]["user_name"] = new_name
            screen.add_to_prompt(f"Cheating: rename player to {new_name}")
        else:
            raise TypeError
    except TypeError:
        print("The new name is not valid")

def add_food(food):
    global data
    data.data["food"][food] += 1
    screen.add_to_prompt(f"Cheating: add {food.lower()}")

def cook_food(food):
    global data
    if food == "Salad":
        data.data["food"]["Vegetable"] += 2
        game.cook(food)
    elif food == "Pescatarian":
        data.data["food"]["Fish"] += 1
        data.data["food"]["Vegetable"] += 1
        game.cook(food)
    elif food == "Roasted":
        data.data["food"]["Meat"] += 1
        data.data["food"]["Vegetable"] += 1
        game.cook(food)
    screen.add_to_prompt(f"Cheating: cook {food.lower()}")


def open_sanctuaries():
    global locations, data
    for key in data.locations.keys():
        data.locations[key]["sanctuaries"]["opened"] == 1     ############# actualizar cuando se tenga hecho locations definitivo
    data.data["character"]["max_hearts"] = 9
    screen.add_to_prompt("Cheating: open sanctuaries")

def game_over():
    global data
    data.data["character"]["hearts_remaining"] = 0
    screen.add_to_prompt("Cheating: game over")

def win_game():
    pass