import os,platform,data

prompt = []

def clear_screen():
    if(platform.system()=="Windows"):
        os.system("cls")
    else:
        os.system("clear")

def add_to_prompt(text):
    prompt.append(text)
    if(len(prompt)>8):
        prompt.pop(0)

def print_prompt():
    for i in range(len(prompt)):
        print(prompt[i])

def print_menu_screen(screen_lines,options,titol_seccio="*"):
    if(len(titol_seccio)%2==0):
        titol_seccio += " "
    options_str = ", ".join(options)
    if(len(options_str)%2==0):
        options_str += " "
    clear_screen()
    print(f"* {titol_seccio} "+"* "*int((77-len(titol_seccio))/2))
    for fila in range(10):
        print("*"+screen_lines[fila].ljust(77)+"*")
    print(f"* {options_str} "+"* "*int((77-len(options_str))/2))
    print_prompt()

def print_screen(char_pos,options,mat,inventory,inv_title="Main",titol_seccio="*"):
    if(inv_title=="Main"):
        inv_title="Inventory"
    if(len(titol_seccio)%2==0):
        titol_seccio += " "
    if(len(inv_title)%2==0):
        inv_title = " " + inv_title
    options_str = ", ".join(options)
    if(len(options_str)%2==0):
        options_str += " "
    clear_screen()
    print(f"* {titol_seccio} "+"* "*int(((77-len(titol_seccio)-len(inv_title))/2)-1)+inv_title+" *")
    for i in range(len(mat)):
        print("*",end="")
        j = 0
        while j < len(mat[i]):
            if(i==char_pos[0] and j==char_pos[1]):
                print("X",end="")
                j += 1
            elif(mat[i][j]=="limit"):
                print(" ",end="")
                j += 1
            elif(mat[i][j]=="S"):
                region = data.data["character"]["region"]
                if([i,j+1] != char_pos and [i,j+2] != char_pos):
                    for sanct,info in data.locations[region]["sanctuaries"].items():
                        if(info[1]==[i,j]):
                            if(info[0]==1):
                                print(f"S{sanct}?",end="")
                                j += 3
                            else:
                                print(f"S{sanct}",end="")
                                j += 2
                elif([i,j+1]==char_pos):
                    for sanct,info in data.locations[region]["sanctuaries"].items():
                        if(info[1]==[i,j]):
                            if(info[0]==1):
                                print(f"SX?",end="")
                                j += 3
                            else:
                                print(f"SX",end="")
                                j += 2
                else:
                    for sanct,info in data.locations[region]["sanctuaries"].items():
                        if(info[1]==[i,j]):
                            print(f"S{sanct}X",end="")
                            j += 3
            elif(mat[i][j]=="E"):
                region = data.data["character"]["region"]
                if([i,j+1]!=char_pos):
                    for enemy in data.locations[region]["enemies"].values():
                        if(enemy[1]==[i,j]):
                            print(f"E{enemy[0]}",end="")
                            j += 2
                else:
                    for enemy in data.locations[region]["enemies"].values():
                        if(enemy[1]==[i,j]):
                            print(f"{enemy[0]}X",end="")
                            j += 2
            elif(mat[i][j]!="!"):
                print(mat[i][j],end="")
                j += 1
            else:
                print(" ",end="")
                j += 1
        print("* ",end="")
        print(inventory[i].ljust(17),end=" *\n")
    if(titol_seccio=="General Map"):
        print(f"* {options} "+"* "*int((77-len(options))/2))
    else:
        print(f"* {options_str} "+"* "*int((77-len(options_str))/2))
    print_prompt()