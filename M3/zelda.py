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
scr.print_screen(initial_screens[cover],options)