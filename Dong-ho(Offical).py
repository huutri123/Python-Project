import pygame
from datetime import datetime
from playsound import playsound
import time
import os
from threading import  Thread

# Windows
pygame.init()

screen = pygame.display.set_mode((400,600))
running = True

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)

a = 0
# b = ''

# def on_click(x, y, button, pressed):
# 		# Định vị con trở
# 		# print('{0} at {1}'.format(
# 		#     'Pressed' if pressed else 'Released',
# 		#     (x, y)))
# 		if not pressed:
# 			# Stop listener
# 			return False

stop_threads = False

def Settime():

	# stop_threads = False

	def validate_time(alarm_time):

		if len(alarm_time) != 11:

			return "Invalid time format! Please try again..."

		else:

			if int(alarm_time[0:2]) > 12:

				return "Invalid HOUR format! Please try again..."

			elif int(alarm_time[3:5]) > 59:

				return "Invalid MINUTE format! Please try again..."

			elif int(alarm_time[6:8]) > 59:

				return "Invalid SECOND format! Please try again..."

			else:

				return "ok"

	while True:

		# alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

		validate = validate_time(alarm_time.lower())

		if validate != "ok":

			print(validate)

		else:

			print(f"Setting alarm for {alarm_time}...")

			break

	alarm_hour = alarm_time[0:2]

	alarm_min = alarm_time[3:5]

	alarm_sec = alarm_time[6:8]

	alarm_period = alarm_time[9:].upper()



	now = datetime.now()

	current_hour = now.strftime("%I")

	current_min = now.strftime("%M")

	current_sec = now.strftime("%S")

	current_period = now.strftime("%p")



	if alarm_period == current_period:

			if alarm_hour == current_hour:

				if alarm_min == current_min:

					if alarm_sec == current_sec:

						print("Wake Up!")

						playsound('D:/AlarmClock.mp3')

	while True:
		now = datetime.now()

		current_hour = now.strftime('%I')

		current_min = now.strftime('%M')

		current_sec = now.strftime('%S')

		current_period = now.strftime("%p")

		if alarm_period == current_period:

			if alarm_hour == current_hour:

				if alarm_min == current_min:

					if alarm_sec == current_sec:

						print("Wake Up!")

						playsound('D:/AlarmClock.mp3')

						break
		
		global stop_threads
		if stop_threads:
			print('stopped')
			break



thread1 = Thread(target = Settime)
	
# Font
font = pygame.font.SysFont('sans', 50)
font_1 = pygame.font.SysFont('sans', 25)

# Time
H = '00'
M = '00'
Ses = '--'
# alarm_time = font.render(str(H) + ':' + str(M) + ':' + str(Ses), True, BLACK)

# Text
text_1 = font_1.render('Set your time', True, BLACK)
text_2 = font_1.render('--------------------------------------------------', True, BLACK)

num1 = font.render('1', True, BLACK)
num2 = font.render('2', True, BLACK)
num3 = font.render('3', True, BLACK)
num4 = font.render('4', True, BLACK)
num5 = font.render('5', True, BLACK)
num6 = font.render('6', True, BLACK)
num7 = font.render('7', True, BLACK)
num8 = font.render('8', True, BLACK)
num9 = font.render('9', True, BLACK)
num0 = font.render('0', True, BLACK)
reset = font_1.render('AC', True, BLACK)
set_up = font_1.render('SET', True, BLACK)

am = font.render('AM', True, BLACK)
pm = font.render('PM', True, BLACK)

while running:
	screen.fill(GREY)

	Time = font.render(datetime.now().strftime("%I:%M:%p"), True, BLACK)

	settime = font.render(str(H) + ':' + str(M) + ':' + str(Ses), True, BLACK)

	alarm_time = str(H) + ':' + str(M) + ':' + '00' + ' ' + str(Ses)

	mouse_x, mouse_y = pygame.mouse.get_pos()
	pygame.draw.rect(screen, WHITE, (20,20,360,100))

	pygame.draw.rect(screen, WHITE, (20,170,360,100))
	screen.blit(settime, (120,190))
	pygame.draw.rect(screen, WHITE, (20,170,360,20))
	pygame.draw.rect(screen, WHITE, (20,250,360,20))
	pygame.draw.rect(screen, GREY, (40,190,60,60))
	pygame.draw.rect(screen, GREY, (300,190,60,60))

	pygame.draw.rect(screen, WHITE, (60,290,60,60))
	pygame.draw.rect(screen, WHITE, (170,290,60,60))
	pygame.draw.rect(screen, WHITE, (280,290,60,60))
	pygame.draw.rect(screen, WHITE, (60,370,60,60))
	pygame.draw.rect(screen, WHITE, (170,370,60,60))
	pygame.draw.rect(screen, WHITE, (280,370,60,60))
	pygame.draw.rect(screen, WHITE, (60,450,60,60))
	pygame.draw.rect(screen, WHITE, (170,450,60,60))
	pygame.draw.rect(screen, WHITE, (280,450,60,60))
	pygame.draw.rect(screen, WHITE, (170,530,60,60))
	pygame.draw.rect(screen, WHITE, (60,530,60,60))
	pygame.draw.rect(screen, WHITE, (280,530,60,60))

	screen.blit(Time, (110,40))
	screen.blit(text_1, (140,125))
	screen.blit(text_2, (25,140))
	screen.blit(set_up, (50,205))
	screen.blit(reset, (313,205))
	screen.blit(num1, (60,290))
	screen.blit(num2, (170,290))
	screen.blit(num3, (280,290))
	screen.blit(num4, (60,370))
	screen.blit(num5, (170,370))
	screen.blit(num6, (280,370))
	screen.blit(num7, (60,450))
	screen.blit(num8, (170,450))
	screen.blit(num9, (280,450))
	screen.blit(num0, (170,530))

	screen.blit(am, (60,530))
	screen.blit(pm, (280,530))

	# with mouse.Listener(
	# 			on_click=on_click,) as listener:
	# 		listener.join()
	# a = a + 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				# NUM 1
				if a == 0 and (60<mouse_x<120) and (290<mouse_y<350):
					H = '01'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '00':
					H = '01'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '01':
					H = '11'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '02':
					H = '21'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '03':
					H = '31'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '04':
					H = '41'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '05':
					H = '51'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '06':
					H = '61'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '07':
					H = '71'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '08':
					H = '81'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (290<mouse_y<350) and H == '09':
					H = '91'
					a = a + 1
					print(a)

				elif a == 2 and (60<mouse_x<120) and (290<mouse_y<350):
					M = '01'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '00':
					M = '01'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '01':
					M = '11'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '02':
					M = '21'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '03':
					M = '31'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '04':
					M = '41'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350) and M == '05':
					M = '51'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (290<mouse_y<350):
					M = '00'
					a = a + 1
					print(a)

				# NUM 2
				if a == 0 and (170<mouse_x<230) and (290<mouse_y<350):
					H = '02'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '00':
					H = '02'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '01':
					H = '12'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '02':
					H = '22'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '03':
					H = '32'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '04':
					H = '42'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '05':
					H = '52'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '06':
					H = '62'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '07':
					H = '72'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '08':
					H = '82'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (290<mouse_y<350) and H == '09':
					H = '92'
					a = a + 1
					print(a)

				elif a == 2 and (170<mouse_x<230) and (290<mouse_y<350):
					M = '02'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '00':
					M = '02'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '01':
					M = '12'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '02':
					M = '22'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '03':
					M = '32'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '04':
					M = '42'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350) and M == '05':
					M = '52'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (290<mouse_y<350):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 3
				if a == 0 and (280<mouse_x<340) and (290<mouse_y<350):
					H = '03'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '00':
					H = '03'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '01':
					H = '13'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '02':
					H = '23'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '03':
					H = '33'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '04':
					H = '43'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '05':
					H = '53'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '06':
					H = '63'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '07':
					H = '73'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '08':
					H = '83'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (290<mouse_y<350) and H == '09':
					H = '93'
					a = a + 1
					print(a)

				elif a == 2 and (280<mouse_x<340) and (290<mouse_y<350):
					M = '03'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '00':
					M = '03'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '01':
					M = '13'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '02':
					M = '23'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '03':
					M = '33'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '04':
					M = '43'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350) and M == '05':
					M = '53'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (290<mouse_y<350):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 4
				if a == 0 and (60<mouse_x<120) and (370<mouse_y<430):
					H = '04'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '00':
					H = '04'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '01':
					H = '14'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '02':
					H = '24'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '03':
					H = '34'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '04':
					H = '44'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '05':
					H = '54'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '06':
					H = '64'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '07':
					H = '74'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '08':
					H = '84'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (370<mouse_y<430) and H == '09':
					H = '94'
					a = a + 1
					print(a)

				elif a == 2 and (60<mouse_x<120) and (370<mouse_y<430):
					M = '04'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '00':
					M = '04'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '01':
					M = '14'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '02':
					M = '24'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '03':
					M = '34'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '04':
					M = '44'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430) and M == '05':
					M = '54'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (370<mouse_y<430):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 5
				if a == 0 and (170<mouse_x<230) and (370<mouse_y<430):
					H = '05'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '00':
					H = '05'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '01':
					H = '15'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '02':
					H = '25'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '03':
					H = '35'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '04':
					H = '45'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '05':
					H = '55'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '06':
					H = '65'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '07':
					H = '75'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '08':
					H = '85'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (370<mouse_y<430) and H == '09':
					H = '95'
					a = a + 1
					print(a)

				elif a == 2 and (170<mouse_x<230) and (370<mouse_y<430):
					M = '05'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '00':
					M = '05'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '01':
					M = '15'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '02':
					M = '25'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '03':
					M = '35'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '04':
					M = '45'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430) and M == '05':
					M = '55'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (370<mouse_y<430):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 6
				if a == 0 and (280<mouse_x<340) and (370<mouse_y<430):
					H = '06'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '00':
					H = '06'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '01':
					H = '16'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '02':
					H = '26'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '03':
					H = '36'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '04':
					H = '46'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '05':
					H = '56'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '06':
					H = '66'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '07':
					H = '76'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '08':
					H = '86'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (370<mouse_y<430) and H == '09':
					H = '96'
					a = a + 1
					print(a)

				elif a == 2 and (280<mouse_x<340) and (370<mouse_y<430):
					M = '06'
					a = a + 1
					print(a)

				elif a == 2 and (280<mouse_x<340) and (370<mouse_y<430):
					M = '06'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '00':
					M = '06'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '01':
					M = '16'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '02':
					M = '26'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '03':
					M = '36'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '04':
					M = '46'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430) and M == '05':
					M = '56'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (370<mouse_y<430):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 7
				if a == 0 and (60<mouse_x<120) and (450<mouse_y<510):
					H = '07'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '00':
					H = '07'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '01':
					H = '17'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '02':
					H = '27'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '03':
					H = '37'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '04':
					H = '47'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '05':
					H = '57'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '06':
					H = '67'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '07':
					H = '77'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '08':
					H = '87'
					a = a + 1
					print(a)
				elif a == 1 and (60<mouse_x<120) and (450<mouse_y<510) and H == '09':
					H = '97'
					a = a + 1
					print(a)

				elif a == 2 and (60<mouse_x<120) and (450<mouse_y<510):
					M = '07'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '00':
					M = '07'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '01':
					M = '17'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '02':
					M = '27'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '03':
					M = '37'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '04':
					M = '47'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510) and M == '05':
					M = '57'
					a = a + 1
					print(a)
				elif a == 3 and (60<mouse_x<120) and (450<mouse_y<510):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 8
				if a == 0 and (170<mouse_x<230) and (450<mouse_y<510):
					H = '08'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '00':
					H = '08'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '01':
					H = '18'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '02':
					H = '28'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '03':
					H = '38'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '04':
					H = '48'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '05':
					H = '58'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '06':
					H = '68'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '07':
					H = '78'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '08':
					H = '88'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (450<mouse_y<510) and H == '09':
					H = '98'
					a = a + 1
					print(a)

				elif a == 2 and (170<mouse_x<230) and (450<mouse_y<510):
					M = '08'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '00':
					M = '08'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '01':
					M = '18'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '02':
					M = '28'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '03':
					M = '38'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '04':
					M = '48'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510) and M == '05':
					M = '58'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (450<mouse_y<510):
					M = '00'
					a = a + 1
					print(a)
				
				# NUM 9
				if a == 0 and (280<mouse_x<340) and (450<mouse_y<510):
					H = '09'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '00':
					H = '09'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '01':
					H = '19'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '02':
					H = '29'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '03':
					H = '39'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '04':
					H = '49'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '05':
					H = '59'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '06':
					H = '69'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '07':
					H = '79'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '08':
					H = '89'
					a = a + 1
					print(a)
				elif a == 1 and (280<mouse_x<340) and (450<mouse_y<510) and H == '09':
					H = '99'
					a = a + 1
					print(a)

				elif a == 2 and (280<mouse_x<340) and (450<mouse_y<510):
					M = '09'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '00':
					M = '09'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '01':
					M = '19'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '02':
					M = '29'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '03':
					M = '39'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '04':
					M = '49'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510) and M == '05':
					M = '59'
					a = a + 1
					print(a)
				elif a == 3 and (280<mouse_x<340) and (450<mouse_y<510):
					M = '00'
					a = a + 1
					print(a)
				

				# AM
				if (60<mouse_x<120) and (530<mouse_y<590):
					Ses = 'AM'

				# NUM 0
				if a == 0 and (170<mouse_x<230) and (530<mouse_y<590):
					H = '00'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '00':
					H = '00'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '01':
					H = '10'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '02':
					H = '20'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '03':
					H = '30'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '04':
					H = '40'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '05':
					H = '50'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '06':
					H = '60'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '07':
					H = '70'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '08':
					H = '80'
					a = a + 1
					print(a)
				elif a == 1 and (170<mouse_x<230) and (530<mouse_y<590) and H == '09':
					H = '90'
					a = a + 1
					print(a)

				elif a == 2 and (170<mouse_x<230) and (530<mouse_y<590) and M == '00':
					M = '00'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '00':
					M = '00'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '00':
					M = '00'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '01':
					M = '10'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '02':
					M = '20'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '03':
					M = '30'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '04':
					M = '40'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590) and M == '05':
					M = '50'
					a = a + 1
					print(a)
				elif a == 3 and (170<mouse_x<230) and (530<mouse_y<590):
					M = '00'
					a = a + 1
					print(a)


				# PM
				if (280<mouse_x<340) and (530<mouse_y<590):
					Ses = 'PM'

				# SET UP TIMER
				if (40<mouse_x<100) and (190<mouse_y<250):
					thread1.start()
					# print(alarm_time)
					# running = False

				# RESET TIMER
				if (300<mouse_x<360) and (190<mouse_y<250):
					a = 0
					M = '00'
					H = '00'
					Ses = '--'
					stop_threads = True

	pygame.display.flip()

pygame.quit()
# def Time():
# 	while running:
# 		screen.fill(WHITE)




# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				running = False

# 		pygame.display.flip()