import os,platform,maps
import inventory as inv

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
        for j in range(len(mat[i])):
            if(i==char_pos[0] and j==char_pos[1]):
                print("X",end="")
            elif(mat[i][j]!="!"):
                print(mat[i][j],end="")
            else:
                print(" ",end="")
        print("* ",end="")
        print(inventory[i].ljust(17),end=" *\n")
    print(f"* {options_str} "+"* "*int((77-len(options_str))/2))
    print_prompt()
