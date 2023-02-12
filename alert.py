import pygame

pygame.init()

running = True

GREY = (150,150,150)

screen = pygame.display.set_mode((500,200))

while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()