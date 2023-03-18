import time
import os
import sys
from pynput.mouse import Button, Controller
from pynput import keyboard


RUTA = "C:/Users/Public/conf.py"
LOOP = True
mouse = Controller()

print('\n=====================================================================')
print('=======Auto Clicker; Desarrollo Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Recuerda*: Para parar el programa pulsa la tecla q\n")
T = int(input(
    "\nSi quieres cargar unos ajustes anteriores pulsa 1, si quieres usar unos nuevos pulsa 2: "))

if T == 2:

    print("\nQuieres que el intervalo se mida en segundos o en milisegundos\n")
    E = input("\nPara milisegundos escribe ms, para segundos escribe s: ")

    A = E.upper()
    list1 = ["S", "SEGUNDO", "SEGUNDOS", "SECONDS"]
    list2 = ["MS", "MILISEGUNDO", "MILISEGUNDOS",
             "MILISECONDS", "MILSEGUNDO", "MILSEGUNDO"]

    while LOOP:
        if A in list1:
            C = float(input(
                "\n¿Cúal quieres que sea el intervalo entre clics medido en segundos?: "))
            LOOP = False
            if C < 0.001:
                C = 0.001
        elif A in list2:
            C = float(input(
                "\n¿Cúal quieres que sea el intervalo entre clics medido en milisegundos?: "))/1000
            LOOP = False
            if C < 0.001:
                C = 0.001
        else:
            print(
                "El fromato de tiempo introducido es incorrecto, porfavor vuelva a intertarlo")

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
