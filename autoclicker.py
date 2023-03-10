from pynput.mouse import Button, Controller
from pynput import keyboard
import time

mouse = Controller()
loop = True
eco = 1
print('\n=====================================================================')
print('=======Auto Clicker; Desarrollo Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Recuerda*: Para parar el programa pulsa la tecla q\n")

while eco >= 0.001:
	cop = float(input("\n¿Cúal quieres que sea el intervalo entre clics medido en segundos?: "))
	if cop >= 0.001:
		eco = 0
	else:
		print("\n\nEl intervalo introducido es muy pequeño, porfavor introduce otro\n\n")

def pulsa(tecla):
	if tecla == keyboard.KeyCode.from_char('q'):
		return False

escuchador = keyboard.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
        mouse.click(Button.left)
        time.sleep(cop)
