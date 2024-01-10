import screen as scr,random,db,datetime,game

initial_screens = ["""                                                                  ## 
                                                                  ## 
                                                               ##~~~ 
                                                              ###~~~O 
 Zelda, Breath of the Wild                                    ###~~~ \ 
                                                               |@@@|  \ 
                                                               |   |   \ 
                                                               =   == 
                                                            %%%%%%%%%%%% 
                                                         %%%%%%%%%%%%%%% """,
"""                                                                  && 
                                                                 oo &
                                                         $       -- &##
                                                         $$     <<OO#### 
 Zelda, Breath of the Wild                                $$  //OOO#### 
                                                           $$// OO#####
                                                            **   OOO### 
                                                             &   @@@@\\
                                                                 Q  Q
                                                                 Q  Q""",
"""                                                                  && 
                                                                 ####
                                                                \" || \"
                                                             @@@@@@@@@@@@ 
 Zelda, Breath of the Wild                                  @     ||@@@ 
                                                                  |@@@
                                                                 @@@ 
                                                               @@@||     @
                                                            @@@@@@@@@@@@@
                                                                  ||"""]

# FUNCIONES AUXILIARES

def check_games():
   db.cur.execute("SELECT count(*) FROM game;")
   query = db.cur.fetchall()
   return query[0][0]

def check_name(name):
   if(len(name)<3 or len(name)>10):
      scr.add_to_prompt(f"'{name}' is not a valid name")
      return False
   else:
      for i in range(len(name)):
         if(not(name[i].isalnum())):
            scr.add_to_prompt(f"'{name}' is not a valid name")
            return False
      return True

def create_game_help():
   while True:
      sec_title = "Help, new game"
      options = ["Back"]
      lines = """

      When asked, type your name and press enter
      if 'Link' is fine for you, just press enter 

      Name must be between 3 and 10 characters long and only 
      letters, numbers and spaces are allowed

      Type 'back' now to go back to 'Set your name'
   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Back"):
         break
      else:
         scr.add_to_prompt("Invalid Action")

def delete_game(id):
      db.cur.execute(f"DELETE FROM game WHERE game_id = {id}")
      db.cur.execute("commit")

def saved_help():
   while True:
      sec_title = "Help, saved games"
      options = ["Back"]
      lines = """

      Type 'play X' to continue playing the game 'X'
      Type 'erase X' to erase the game 'X'
      Type 'back' now to go back to the main menu 
      


      Type 'back' now to go back to 'Saved games'
   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Back"):
         break
      else:
         scr.add_to_prompt("Invalid Action")

# FUNCIONES MENÚ

def menu_help():
   while True:
      sec_title = "Help, main menu"
      options = ["Back"]
      lines = """

      Type 'continue' to continue a saved game
      Type 'new game' to start a new game
      Type 'about' to see information about the game
      Type 'exit' to exit the game


      Type 'back' now to go back to the 'Main menu'
   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Back"):
         break
      else:
         scr.add_to_prompt("Invalid Action")

def about():
   while True:
      sec_title = "About"
      options = ["Back"]
      lines = """

      Game developed by 'OcarinaOfCode'
         
         Marc Arqués
         Adrián Casado
         Joel Martínez

      Type 'back' now to go back to the 'Main menu'
   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Back"):
         break
      else:
         scr.add_to_prompt("Invalid Action")

def create_game():
   lines = """

   

         Set your name?


         
         Type 'back' now to go back to the 'Main menu'
""".split("\n")
   options = ["Back","Help"]
   sec_title = "New Game"
   while True:
      scr.print_menu_screen(lines,options,sec_title)
      try:
         x = input("What to do now? ")
         if(x.capitalize() == "Back"):
            break
         elif(x.capitalize() == "Help"):
            create_game_help()
         elif(x == ""):
            legend()
            break
         elif(check_name(x)):
            scr.add_to_prompt(f"Welcome to the game, {x}")
            legend(x)
            break
         else:
            raise ValueError("Invalid Action")
      except ValueError as e:
         scr.add_to_prompt(e)

def legend(name="Link"):
   while True:
      sec_title = "Legend"
      options = ["Continue"]
      lines = """   10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah
   tribe. The Sheikah were a tribe of warriors who protected the Triforce, 
   a sacred relic that granted wishes. 

   But one day, Ganondorf, an evil sorcerer, stole the Triforce and began 
   to rule Hyrule with an iron fist.

   The princess, with the help of a heroic young man, managed to defeat 
   Ganondorf and recover the Triforce.
   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Continue"):
         break
      else:
         scr.add_to_prompt("Invalid Action")
   plot(name)

def plot(name):
   while True:
      sec_title = "Plot"
      options = ["Continue"]
      lines = f"""       
      
   Now history is repeating itself, and Princess Zelda has been captured by 
   Ganon. He has taken over the Guardians and filled Hyrule with monsters. 


   But a young man named '{name}' has just awakened and 
   must reclaim the Guardians to defeat Ganon and save Hyrule. 

   """.split("\n")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ")
      if(x.capitalize()=="Continue"):
         scr.add_to_prompt("The adventure begins")
         new_game(name)
         break
      else:
         scr.add_to_prompt("Invalid Action")

def new_game(user_name):
   insert = 'INSERT INTO game (user_name,last_connected,hearts_remaining,max_hearts,blood_moon_countdown,blood_moon_appearances,region) VALUES (%s,%s,%s,%s,%s,%s,%s);'
   values = (user_name,datetime.datetime.now(),3,3,25,0,"Hyrule")
   db.cur.execute(insert,values)
   db.connection.commit()

def saved_games():
   while True:
      sec_title = "Saved games"
      options = ["Play X","Erase X","Help","Back"]
      games = {}
      db.cur.execute("SELECT game_id FROM game")
      ids = db.cur.fetchall()
      for game_id in ids:
         db.cur.execute(f"SELECT * FROM game WHERE game_id = {game_id[0]};")
         query = db.cur.fetchall()
         print(query[0][2])
         games[game_id] = {
            "id" : game_id[0],
            "date" : query[0][2],
            "name" : query[0][1],
            "region" : query[0][7], # !!!!!!!!!!!!!!!!!!!!!!! MODIFICAR CUANDO ESTE LA BBDD DEFINITIVA
            "act_hearts" : query[0][3],
            "total_hearts" : query[0][4]  # !!!!!!!!!!!!!!!!!!!!!!!! MODIFICAR CUANDO ESTE LA BBDD DEFINITIVA
         }
      lines = [""]
      # games.sort(reverse=True,key=lambda x:x["date"])
      for i in range(len(games)):
         key = list(games.keys())[i]
         lines.append(f" {key[0]}: {games[key]['date'].day}/{games[key]['date'].month}/{games[key]['date'].year} {games[key]['date'].hour}:{games[key]['date'].minute}:{games[key]['date'].second} - {games[key]['name']}, {games[key]['region']}".ljust(71)+f"♥ {games[key]['act_hearts']}/{games[key]['total_hearts']} ")
      while(len(lines)<10):
         lines.append("")
      scr.print_menu_screen(lines,options,sec_title)
      x = input("What to do now? ").split(" ")
      try:
         ids_ok = []
         for i in range(len(ids)):
            ids_ok.append(ids[i][0])
         if(x[0].capitalize()=="Play" and len(x)==2):
            if(int(x[1]) in ids_ok):
               db.cur.execute("SELECT region FROM game;")
               game_info = db.cur.fetchall()
               game.play(int(x[1]),game_info[0][0])
               break
            raise ValueError("Invalid Action")
         elif(x[0].capitalize()=="Erase" and len(x)==2):
            if(int(x[1]) in ids_ok):
               delete_game(int(x[1]))
               break
            raise ValueError(f"Invalid Action")
         elif(x[0].capitalize()=="Help" and len(x)==1):
            saved_help()
         elif(x[0].capitalize()=="Back" and len(x)==1):
            break
         else:
            raise ValueError("Invalid Action")
      except ValueError as e:
         scr.add_to_prompt(e)
      
# EJECUCIÓN JUEGO

options = ["Continue","New Game","Help","About","Exit"]
cover = random.randint(0,len(initial_screens)-1)
screen_lines = initial_screens[cover].split("\n")

while True:
   if(check_games()==0):
      options.pop(0)
   scr.print_menu_screen(screen_lines,options)
   try:
      x = input("What to do now? ")
      opt = x.split(" ")
      if(opt[0].capitalize() not in options):
         if(len(opt)==1):
            raise ValueError("Invalid Action")
         if((opt[0].capitalize() + " " + opt[1].capitalize()) not in options):
            raise ValueError("Invalid Action")
         
      if(opt[0].capitalize()=="Help"):
         menu_help()
      elif(opt[0].capitalize()=="Exit"):
         break
      elif(opt[0].capitalize()=="About"):
         about()
      elif(opt[0].capitalize()=="Continue"):
         if(check_games()>1):
            saved_games()
         else:
            db.cur.execute("SELECT game_id FROM game;")
            game_id = db.cur.fetchall()[0][0]
            db.cur.execute(f"SELECT region FROM game WHERE game_id={game_id};")
            act_location = db.cur.fetchall()[0][0]
            game.play(game_id,act_location)
            break
      elif(opt[0].capitalize()=="New" and opt[1].capitalize()=="Game"):
         create_game()
   except ValueError as e:
      scr.add_to_prompt(e)