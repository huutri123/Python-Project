import pygame
from random import randint

start = False
running = True
lock = True

# player = 'a'
computer = randint(0,2)


# Windown
pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)


font = pygame.font.SysFont('sans', 50)
font_1 = pygame.font.SysFont('sans', 25)

# Set up
text_1 = font_1.render('Chon Bua, Keo, Bao', True, BLACK)
text_2 = font.render('Bua', True, BLACK)
text_3 = font.render('Keo', True, BLACK)
text_4 = font.render('Bao', True, BLACK)
text_5 = font.render('Reset', True, BLACK)

text_6 = font_1.render('--------------------------------------------------', True, BLACK)

# Game
text_win = font.render('You Win', True, BLACK)
text_lose = font.render('You Lose', True, BLACK)
text_draw = font.render('Draw', True, BLACK)

text_player = ''
answer_player1 = font_1.render('Bua', True, BLACK)
answer_player2 = font_1.render('Keo', True, BLACK)
answer_player3 = font_1.render('Bao', True, BLACK)

text_computer = ''


while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (50,50,400,250))
	pygame.draw.rect(screen, WHITE, (50,400,100,100))
	pygame.draw.rect(screen, WHITE, (200,400,100,100))
	pygame.draw.rect(screen, WHITE, (350,400,100,100))
	pygame.draw.rect(screen, WHITE, (175,525,150,50))

	screen.blit(text_1, (150,50))
	screen.blit(text_2, (50,400))
	screen.blit(text_3, (200,400))
	screen.blit(text_4, (350,400))
	screen.blit(text_5, (175,525))

	screen.blit(text_6, (75,65))

	# screen.blit(text_player, (50,90))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (50 < mouse_x < 150) and (400 < mouse_y < 500) and lock:
					start = True
					player = 'Bua'
					lock = False
					# screen.blit(font.render('sdjfhsdjkf', True, BLACK), (100,200))
				if (200 < mouse_x < 300) and (400 < mouse_y < 500) and lock:
					start = True
					player = 'Keo'
					lock = False
				if (350 < mouse_x < 450) and (400 < mouse_y < 500) and lock:
					start = True
					player = 'Bao'
					lock = False
				if (175 < mouse_x < 325) and (525 < mouse_y < 575):
					start = False
					computer = randint(0,2)
					lock = True


	if start:
		# Bua, Keo ,Bao
		# player = 0
		# computer = randint(0,2)

		text_player = font_1.render('You choose: ' + str(player), True, BLACK)
		text_computer = font_1.render('Compter choose: ' + str(computer), True, BLACK)

		screen.blit(text_player, (75,90))
		
		screen.blit(text_computer, (75, 110))


		if computer == 0:
			computer = 'Bua'
		if computer == 1:
			computer = 'Bao'
		if computer == 2:
			computer = 'Keo'

		# print('----')
		# print('You choose: ' + player)
		# print('Compter choose: ' + computer)
		# print('----')

		if player == computer:
			screen.blit(text_6, (75,125))
			screen.blit(text_draw, (200,190))
		else:
			if player == 'Keo':
				if computer == 'Bua':
					screen.blit(text_6, (75,125))
					screen.blit(text_lose, (165,190))
				else:
					screen.blit(text_6, (75,125))
					screen.blit(text_win, (170,190))

			elif player == 'Bua':
				if computer == 'Bao':
					screen.blit(text_6, (75,125))
					screen.blit(text_lose, (165,190))
				else:
					screen.blit(text_6, (75,125))
					screen.blit(text_win, (170,190))

			elif player == 'Bao':
				if computer == 'Bua':
					screen.blit(text_6, (75,125))
					screen.blit(text_win, (170,190))
				else:
					screen.blit(text_6, (75,125))
					screen.blit(text_lose, (165,190))


	pygame.display.flip()

pygame.quit()