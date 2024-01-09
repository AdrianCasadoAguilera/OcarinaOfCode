import os,platform,maps

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

def print_screen(options,mat,titol_seccio="*"):
    if(len(titol_seccio)%2==0):
        titol_seccio += " "
    options_str = ", ".join(options)
    if(len(options_str)%2==0):
        options_str += " "
    clear_screen()
    print(f"* {titol_seccio} "+"* "*int((77-len(titol_seccio))/2))
    for i in range(len(mat)):
        print("*",end="")
        for j in range(len(mat[i])):
            print(mat[i][j],end="")
        print("* ",end="")

    print(f"* {options_str} "+"* "*int((77-len(options_str))/2))
    print_prompt()

options = ["Back"]
titol_seccio = "Map"
mat = maps.prueba

print_screen(options,mat,titol_seccio)