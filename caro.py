import pygame
from random import randint

# Window
pygame.init()

screen = pygame.display.set_mode((400,500))

GREY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)

font = pygame.font.SysFont('sans', 100)

running = True
start = False
look1 = True
look2 = True
look3 = True
look4 = True
look5 = True
look6 = True
look7 = True
look8 = True
look9 = True

block_1 = ''
block_2 = ''
block_3 = ''
block_4 = ''
block_5 = ''
block_6 = ''
block_7 = ''
block_8 = ''
block_9 = ''

computerChoose_1 = ''
computerChoose_2 = ''
computerChoose_3 = ''
computerChoose_4 = ''
computerChoose_5 = ''
computerChoose_6 = ''
computerChoose_7 = ''
computerChoose_8 = ''
computerChoose_9 = ''

# block1 = font.render(block_1, True, BLACK)
# block2 = font.render(block_2, True, BLACK)
# block3 = font.render(block_3, True, BLACK)
# block4 = font.render(block_4, True, BLACK)
# block5 = font.render(block_5, True, BLACK)
# block6 = font.render(block_6, True, BLACK)
# block7 = font.render(block_7, True, BLACK)
# block8 = font.render(block_8, True, BLACK)
# block9 = font.render(block_9, True, BLACK)


# Random
computer = randint(0,8)



while running:
	screen.fill(GREY)

	mouse_x,mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (40,50,100,100))
	pygame.draw.rect(screen, WHITE, (150,50,100,100))
	pygame.draw.rect(screen, WHITE, (260,50,100,100))
	pygame.draw.rect(screen, WHITE, (40,160,100,100))
	pygame.draw.rect(screen, WHITE, (150,160,100,100))
	pygame.draw.rect(screen, WHITE, (260,160,100,100))
	pygame.draw.rect(screen, WHITE, (40,270,100,100))
	pygame.draw.rect(screen, WHITE, (150,270,100,100))
	pygame.draw.rect(screen, WHITE, (260,270,100,100))

	# screen.blit(block1, (60,41))
	# screen.blit(block2, (170,41))
	# screen.blit(block3, (280,41))
	# screen.blit(block4, (60,151))
	# screen.blit(block5, (170,151))
	# screen.blit(block6, (280,151))
	# screen.blit(block7, (60,261))
	# screen.blit(block8, (170,261))
	# screen.blit(block9, (280,261))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:

				if (40 < mouse_x < 140) and (50 < mouse_y < 150) and look1:
					start = True
					computer = randint(0,8)
					block_1 = 'X'
					look1 = False
				if (150 < mouse_x < 260) and (50 < mouse_y < 150) and look2:
					start = True
					computer = randint(0,8)
					block_2 = 'X'
					look2 = False
				if (270 < mouse_x < 380) and (50 < mouse_y < 150) and look3:
					start = True
					computer = randint(0,8)
					block_3 = 'X' and look5
					look3 = False
				if (40 < mouse_x < 140) and (160 < mouse_y < 270) and look4:
					start = True
					computer = randint(0,8)
					block_4 = 'X'
					look4 = False
				if (150 < mouse_x < 260) and (160 < mouse_y < 270) and look5:
					start = True
					computer = randint(0,8)
					block_5 = 'X'
					look5 = False
				if (270 < mouse_x < 380) and (160 < mouse_y < 270) and look6:
					start = True
					computer = randint(0,8)
					block_6 = 'X'
					look6 = False
				if (40 < mouse_x < 140) and (280 < mouse_y < 390) and look7:
					start = True
					computer = randint(0,8)
					block_7 = 'X'
					look7 = False
				if (150 < mouse_x < 260) and (280 < mouse_y < 390) and look8:
					start = True
					computer = randint(0,8)
					block_8 = 'X'
					look8 = False
				if (270 < mouse_x < 380) and (280 < mouse_y < 390) and look9:
					start = True
					computer = randint(0,8)
					block_9 = 'X'
					look9 = False

	if start:

		block1 = font.render(block_1, True, BLACK)
		block2 = font.render(block_2, True, BLACK)
		block3 = font.render(block_3, True, BLACK)
		block4 = font.render(block_4, True, BLACK)
		block5 = font.render(block_5, True, BLACK)
		block6 = font.render(block_6, True, BLACK)
		block7 = font.render(block_7, True, BLACK)
		block8 = font.render(block_8, True, BLACK)
		block9 = font.render(block_9, True, BLACK)

		screen.blit(block1, (60,41))
		screen.blit(block2, (170,41))
		screen.blit(block3, (280,41))
		screen.blit(block4, (60,151))
		screen.blit(block5, (170,151))
		screen.blit(block6, (280,151))
		screen.blit(block7, (60,261))
		screen.blit(block8, (170,261))
		screen.blit(block9, (280,261))

		computerChoose1 = font.render(computerChoose_1, True, BLACK)
		computerChoose2 = font.render(computerChoose_2, True, BLACK)
		computerChoose3 = font.render(computerChoose_3, True, BLACK)
		computerChoose4 = font.render(computerChoose_4, True, BLACK)
		computerChoose5 = font.render(computerChoose_5, True, BLACK)
		computerChoose6 = font.render(computerChoose_6, True, BLACK)
		computerChoose7 = font.render(computerChoose_7, True, BLACK)
		computerChoose8 = font.render(computerChoose_8, True, BLACK)
		computerChoose9 = font.render(computerChoose_9, True, BLACK)

		screen.blit(computerChoose1, (60,41))
		screen.blit(computerChoose2, (170,41))
		screen.blit(computerChoose3, (280,41))
		screen.blit(computerChoose4, (60,151))
		screen.blit(computerChoose5, (170,151))
		screen.blit(computerChoose6, (280,151))
		screen.blit(computerChoose7, (60,261))
		screen.blit(computerChoose8, (170,261))
		screen.blit(computerChoose9, (280,261))

		if computer == 0 and look1:
			computerChoose_1 = 'O'
			look1 = False
		if computer == 1 and look2:
			computerChoose_2 = 'O'
			look2 = False
		if computer == 2 and look3:
			computerChoose_3 = 'O'
			look3 = False
		if computer == 3 and look4:
			computerChoose_4 = 'O'
			look4 = False
		if computer == 4 and look5:
			computerChoose_5 = 'O'
			look5 = False
		if computer == 5 and look6:
			computerChoose_6 = 'O'
			look6 = False
		if computer == 6 and look7:
			computerChoose_7 = 'O'
			look7 = False
		if computer == 7 and look8:
			computerChoose_8 = 'O'
			look8 = False
		if computer == 8 and look9:
			computerChoose_9 = 'O'
			look9 = False

	pygame.display.flip()