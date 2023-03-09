from pynput.mouse import Button, Controller
from pynput import keyboard
import time

mouse = Controller()
loop = True
print('\n=====================================================================')
print('=======Auto Clicker; Developed Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Remember*: To stop the program press the key q\n")

eco = float(input("\nHow many clickcs for interval do you want, measured in seconds: "))
def pulsa(tecla):
	if tecla == keyboard.KeyCode.from_char('q'):
		return False

escuchador = keyboard.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
        mouse.click(Button.left)
        time.sleep(eco)
