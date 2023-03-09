from pynput.mouse import Button, Controller
from pynput import keyboard
import time

mouse = Controller()
loop = True
print('\n=====================================================================')
print('=======Auto Clicker; Desarrollo Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Recuerda*: Para parar el programa pulsa la tecla q\n")

eco = float(input("\n¿Cúal quieres que sea el intervalo entre clics? Medido en segundos: "))
def pulsa(tecla):
	if tecla == keyboard.KeyCode.from_char('q'):
		return False

escuchador = keyboard.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
        mouse.click(Button.left)
        time.sleep(eco)
