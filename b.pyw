from datetime import datetime
from playsound import playsound
import time

now = datetime.now()
H = now.strftime("%I")
M = now.strftime("%M")
Ses = now.strftime("%p")

while True:

	now = datetime.now()
	H = now.strftime("%I")
	M = now.strftime("%M")
	Ses = now.strftime("%p")

	Time = datetime.now().strftime("%I:%M:%p")
	
	# if M != "%M":
	# 	print(Time)

	if H == "06" and M == "00" and Ses == "PM":
		print(Time)
		playsound('D:/AlarmClock.mp3')
		time.sleep(60)
		continue
	if H == "06" and M == "30" and Ses == "PM":
		print(Time)
		playsound('D:/AlarmClock.mp3')
		time.sleep(60)
		continue
	if H == "07" and M == "00" and Ses == "PM":
		print(Time)
		playsound('D:/AlarmClock.mp3')
		time.sleep(60)
		continue
	elif H == "09" and M == "15":
		print(Time)
		playsound('D:/AlarmClock.mp3')
		time.sleep(60)
		continue
	elif H == "10" and M == "00" and Ses == "PM":
		print(Time)
		playsound('D:/AlarmClock.mp3')
		# time.sleep(60)
		break