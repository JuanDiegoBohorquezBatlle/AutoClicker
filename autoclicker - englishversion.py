import time
import os
import sys
from pynput.mouse import Button, Controller
from pynput import keyboard


RUTA = "C:/Users/Public/conf.py"
LOOP = True
mouse = Controller()

print('\n=====================================================================')
print('=======Auto Clicker; Developed Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Remember*: To stop the program press the key q\n")

T = int(input(
    "\nIf you want use the previous adjusts press 1, if you want new adjust press 2: "))

if T == 2:

    print("\nDo you want the interval to be measured in seconds or in milliseconds?\n")
    E = input("\For milliseconds write ms, for seconds write s: ")

    A = E.upper()
    list1 = ["S", "SEGUNDO", "SEGUNDOS", "SECONDS", "SECOND"]
    list2 = ["MS", "MILISEGUNDO", "MILISEGUNDOS",
             "MILISECOND", "MILISECONDS", "MILLISECONDS", "MILLISECOND"]

    while LOOP:
        if A in list1:
            C = float(input(
                "\nHow many clickcs for interval do you want? Measured in seconds: "))
            LOOP = False
            if C < 0.001:
                C = 0.001
        elif A in list2:
            C = float(input(
                "\nHow many clickcs for interval do you want? Measured in milliseconds: "))/1000
            LOOP = False
            if C < 0.001:
                C = 0.001
        else:
            print(
                "The time format introduced is incorrect, please try again")

        CONT = f"C = {str(C)}"

        with open(RUTA, "w", encoding="utf-8") as archivo:
            archivo.write(CONT)

if os.path.exists(RUTA):
    sys.path.insert(0, "C:/Users/Public")
    from conf import C


def pulsa(tecla):
    if tecla == keyboard.KeyCode.from_char('q'):
        return False


escuchador = keyboard.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
    mouse.click(Button.left)
    time.sleep(C)
