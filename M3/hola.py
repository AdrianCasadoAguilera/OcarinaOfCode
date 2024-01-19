import maps, math, data, db

def collect_data(id):
    for region in data.locations.keys():
        db.cur.execute(f"SELECT * FROM enemies WHERE game_id = {id} AND region = '{region}'")
        rst = db.cur.fetchall()
        for i in (rst):
            data.locations[region]["enemies"][i[2]] = [i[5], [i[3],i[4]]]

        db.cur.execute(f"SELECT * FROM trees WHERE game_id = {id} AND region = '{region}'")
        rst = db.cur.fetchall()
        for i in (rst):
            if i[5] != 0:
                data.locations[region]["trees"][i[2]] = [i[5], [i[3],i[4]]]
            else:
                data.locations[region]["trees"][i[2]] = [-i[6], [i[3],i[4]]]

        db.cur.execute(f"SELECT * FROM chests WHERE game_id = {id} AND region = '{region}'")
        rst = db.cur.fetchall()
        for i in (rst):
            data.locations[region]["chests"][i[2]] = [i[3], [i[4],i[5]]]

        db.cur.execute(f"SELECT * FROM sanctuaries WHERE game_id = {id} AND region = '{region}'")
        rst = db.cur.fetchall()
        for i in (rst):
            data.locations[region]["sanctuaries"][i[2]] = [i[5], [i[3],i[4]]]