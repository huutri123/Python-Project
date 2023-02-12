import pygame
from datetime import datetime
import math
from threading import Thread

pygame.init()

screen = pygame.display.set_mode((400,600))

running = True

font = pygame.font.SysFont('sans', 50)
font_1 = pygame.font.SysFont('sans', 25)

GREY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)

num1 = font_1.render('1', True, BLACK)
num2 = font_1.render('2', True, BLACK)
num3 = font_1.render('3', True, BLACK)
num4 = font_1.render('4', True, BLACK)
num5 = font_1.render('5', True, BLACK)
num6 = font_1.render('6', True, BLACK)
num7 = font_1.render('7', True, BLACK)
num8 = font_1.render('8', True, BLACK)
num9 = font_1.render('9', True, BLACK)
num10 = font_1.render('10', True, BLACK)
num11 = font_1.render('11', True, BLACK)
num12 = font_1.render('12', True, BLACK)

while running:
	screen.fill(GREY)

	Time = font.render(datetime.now().strftime("%I:%M:%p"), True, BLACK)

	mins1 = 12

	now = datetime.now()
	secs = float(now.strftime("%S"))
	mins = float(now.strftime("%M"))
	hours = float(now.strftime("%I"))

	pygame.draw.circle(screen, BLACK,(200,150),100)
	pygame.draw.circle(screen, WHITE,(200,150),95)
	pygame.draw.circle(screen, BLACK,(200,150),5)

	x_min = 200 + 80* math.sin(6* mins * math.pi/180)
	y_min = 150 - 80* math.cos(6* mins * math.pi/180)
	pygame.draw.line(screen, BLACK, (200,150),(x_min,y_min))

	if mins >= mins1:
		hours = hours + 0.2
		mins1 = mins1 + 12
	if mins >= mins1:
		hours = hours + 0.2
		mins1 = mins1 + 12
	if mins >= mins1:
		hours = hours + 0.2
		mins1 = mins1 + 12
	if mins >= mins1:
		hours = hours + 0.2
		mins1 = mins1 + 12

	x_hour = 200 + 50* math.sin(30* hours * math.pi/180)
	y_hour = 150 - 50* math.cos(30* hours * math.pi/180)
	pygame.draw.line(screen, BLACK, (200,150),(x_hour,y_hour))

	screen.blit(Time, (100,400))

	screen.blit(num1, (232,69))
	screen.blit(num2, (261,98))
	screen.blit(num3, (272,138))
	screen.blit(num4, (261,178))
	screen.blit(num5, (232,207))
	screen.blit(num6, (192,218))
	screen.blit(num7, (152,206))
	screen.blit(num8, (123,178))
	screen.blit(num9, (112,138))
	screen.blit(num10, (123,98))
	screen.blit(num11, (152,69))
	screen.blit(num12, (192,58))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()