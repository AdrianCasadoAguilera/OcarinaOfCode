import os,platform

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

def print_screen(screen,options):
    screen_lines = screen.split("\n")
    options_str = ", ".join(options)
    clear_screen()
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    for fila in range(10):
        print("*"+screen_lines[fila].ljust(77)+"*")
    print(f"* {options_str} "+"* "*int((77-len(options_str))/2))
    print_prompt()