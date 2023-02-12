import pygame

running = True

pygame.init()

screen = pygame.display.set_mode((400,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)

while running:
	screen.fill(GREY)

	pygame.draw.rect(screen, WHITE, (25,20,350,100))

	pygame.draw.circle(screen, WHITE, (200,180), 50)

	pygame.draw.circle(screen, BLACK, (200,150), 10)
	pygame.draw.circle(screen, BLACK, (200,210), 10)
	pygame.draw.circle(screen, BLACK, (170,180), 10)
	pygame.draw.circle(screen, BLACK, (230,180), 10)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print('XXX')

	pygame.display.flip()

pygame.quit()
