from pynput.mouse import Button, Controller
from pynput import keyboard
import time

mouse = Controller()
loop = True
eco = 1

print('\n=====================================================================')
print('=======Auto Clicker; Developed Juan Diego Bohorquez Batlle==========')
print('=====================================================================\n')

print("\n*Remember*: To stop the program press the key q\n")

while eco >= 0.001:
	cop = float(input("\nHow many clickcs for interval do you want? Measured in seconds: "))

	if cop >= 0.001:
		eco = 0
	else:
		print("\n\nThe interval it is too small, please try again\n\n")
def pulsa(tecla):
	if tecla == keyboard.KeyCode.from_char('q'):
		return False

escuchador = keyboard.Listener(pulsa)
escuchador.start()

while escuchador.is_alive():
        mouse.click(Button.left)
        time.sleep(cop)
