import db

def initialize_data(id):
    global data 
    data = {
        "character" : {
            "game_id" : id,
            "user_name" : db.user_name(id),
            "hearts_remaining" : db.actual_hearts(id),
            "max_hearts" : db.max_hearts(id),
            "region" : db.region(id),
            "blood_moon_countdown" : db.blood_moon_countdown(id)
        },
        "foods" : {
            "Meat" : db.food_totals(id)["Meat"],
            "Fish" : db.food_totals(id)["Fish"],
            "Vegetable" : db.food_totals(id)["Vegetable"],
            "Pescatarian" : db.food_totals(id)["Pescatarian"],
            "Roasted" : db.food_totals(id)["Roasted"],
            "Salad" : db.food_totals(id)["Salad"]
        }
    }

locations = {
    "Hyrule": {
        "enemies" : {
            1 : [1,[20,8]],
            2 : [9,[25,4]]
        },
        "chests": {
            1 : [48,9]
        },        
        "fishing" : 1
        },    
    "Death Mountain" : {
        "enemies":{
            1 : [2,[13,4]],
            2 : [2,[51,3]]
        },
        "chests": {
            1 : [36,8]
        },
        "fishing" : 1
    },
    "Gerudo": {
        "enemies": {
            1: [1, [2, 3]],
            2: [2, [37, 5]]
        },
        "chests": {
            1 : [52,1],
            2 : [8,9]
        },
        "fishing" : 1
    },    
    "Necluda" : {
        "enemies" : {
            1 : [1,[10,2]],
            2 : [2,[38,6]]
        },
        "chests": {
            1 : [22,1],
            2 : [51,2],
            3 : [23,9]
        },
        "fishing" : 1
    }
}
