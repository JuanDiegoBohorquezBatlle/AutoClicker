import time
import os
import sys
from pynput.mouse import Button, Controller
from pynput import keyboard

paused = False
RUTA = "C:/Users/Public/AutoClicker/conf.py"
LOOP = True
a = 0
mouse = Controller()

print('\n=====================================================================')
print('=======Auto Clicker; Desarrollo Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Recuerda*: Para parar el programa pulsa la tecla q\n            O para pausarlo utiliza la tecla espacio")
T = int(input(
    "\nSi quieres cargar unos ajustes anteriores pulsa 1, si quieres usar unos nuevos pulsa 2: "))

while LOOP:
    if a == 1:
        T = 2
        a = 0
    else:
        if T == 2:
            while LOOP:
                print(
                    "\nQuieres que el intervalo se mida en segundos o en milisegundos\n")
                while LOOP:
                    E = input(
                        "\nPara milisegundos escribe ms, para segundos escribe s: ")

                    A = E.upper()
                    list1 = ["S", "SEGUNDO", "SEGUNDOS", "SECONDS"]
                    list2 = ["MS", "MILISEGUNDO", "MILISEGUNDOS",
                             "MILISECONDS", "MILSEGUNDO", "MILSEGUNDOS"]

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
                            "\nEl formato de tiempo introducido es incorrecto, porfavor vuelva a intertarlo")

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
                "\nNo has usado este programa antes, porfavor cree un nuevo intervalo\n\n")
            a = 1


def on_press(tecla):
    global paused
    if tecla == keyboard.Key.space:
        if paused:
            paused = False
        else:
            paused = True
    if tecla == keyboard.KeyCode.from_char('q'):
        return False


escuchador = keyboard.Listener(on_press)
escuchador.start()

input('presiona ENTER cuando quieras empezar')

while escuchador.is_alive():
    if paused == False:
        mouse.click(Button.left)
        time.sleep(C)
