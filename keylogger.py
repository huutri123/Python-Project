from pynput.keyboard import Listener
from pynput import mouse

a = 0


def on_click(x, y, button, pressed):
	if not pressed:
		# Stop listener
		return False
	a = a + 1
	print(a)


with mouse.Listener(
		on_click=on_click,) as listener:
	listener.join()


def anonumous(key):
	key = str(key)
	key = key.replace("'","")
	
	key = key.replace("Key.ctrl_l","")
	key = key.replace("Key.ctrl_r","")
	key = key.replace("Key.alt_l","\n")
	key = key.replace("Key.alt_r","\n")
	key = key.replace("Key.tab","\n")

	if key == "Key.f12":
		raise SystemExit(0)

	# if key == "Key.ctrl_l":
	# 	key = ""

	# if key == "":
	# 	pass

	# with open("log.txt", "a") as file:
	# 	file.write(key)
	print(key)


with Listener(on_press=anonumous) as listener:
	listener.join()

