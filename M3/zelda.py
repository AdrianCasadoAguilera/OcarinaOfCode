import screen as scr,random

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

options = ["Continue","New Game","Help","About","Exit"]

cover = random.randint(0,len(initial_screens)-1)
screen_lines = initial_screens[cover].split("\n")
scr.print_screen(screen_lines,options,titol_seccio="*")