import time
import os
import sys
from pynput.mouse import Button, Controller
from pynput import keyboard

paused = False
RUTA = "C:/Users/Public/AutoClicker/conf.py"
LOOP = True
list1 = ["S", "SEGUNDO", "SEGUNDOS", "SECONDS", "SECOND"]
list2 = ["MS", "MILISEGUNDO", "MILISEGUNDOS",
             "MILISECOND", "MILISECONDS", "MILLISECONDS", "MILLISECOND"]
a = 0
mouse = Controller()

print('\n=====================================================================')
print('=======Auto Clicker; Developed Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Remember*: To stop the program press the key q\n")

T = int(input(
    "\nIf you want use the previous adjusts press 1, if you want new adjust press 2: "))

while LOOP:
    if a == 1:
        T = 2
        a = 0
    else:
        if T == 2:
            while LOOP:
                print(
                    "\nDo you want the interval to be measured in seconds or in milliseconds?\n")
                while LOOP:
                    E = input(
                        "\nFor milliseconds write ms, for seconds write s: ")
                    
                    E = E.upper()
    
                    if E in list1:
                        C = float(input(
                            "\nHow many clickcs for interval do you want? Measured in seconds: "))
                        LOOP = False
                        if C < 0.001:
                            C = 0.001
                            
                    elif E in list2:
                        C = float(input(
                            "\nHow many clickcs for interval do you want? Measured in milliseconds: "))/1000
                        LOOP = False
                        if C < 0.001:
                            C = 0.001
                    else:
                        print(
                            "The time format introduced is incorrect, please try again")

                CONT = f"C = {str(C)}"
                if not os.path.exists("C:/Users/Public/AutoClicker/"):
                    os.makedirs("C:/Users/Public/AutoClicker/")
                with open(RUTA, "w", encoding="utf-8") as archivo:
                    archivo.write(CONT)

        elif os.path.exists(RUTA):
            sys.path.insert(0, "C:/Users/Public/AutoClicker/")
            from conf import C
            LOOP = False
        else:
            print(
                "\nYou did not have use this programm before, please create a new interval\n\n")
            a = 1


def press(tecla):
    global paused
    if tecla == keyboard.Key.space:
        if paused:
            paused = False
        else:
            paused = True
    if tecla == keyboard.KeyCode.from_char('q'):
        return False

escuchador = keyboard.Listener(press)
escuchador.start()

while escuchador.is_alive():
    if paused == False:
        mouse.click(Button.left)
        time.sleep(C)
