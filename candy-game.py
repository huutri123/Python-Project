import pygame

pygame.init()

screen = pygame.display.set_mode((400,600))

running = True

GREY = (150,150,150)
WHITE = (255,255,255)

# Animation
pic = pygame.image.load("logo.png")
pic1 = pygame.transform.scale(pic, (45,45))

start = False
timer = pygame.time.Clock()

picx = 25
picy = 25

speedx = 1
speedy = 1

while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (10,10,380,435))
	pygame.draw.rect(screen, GREY, (15,15,370,425))

	pygame.draw.rect(screen, WHITE, (25,20,50,50))
	pygame.draw.rect(screen, WHITE, (85,20,50,50))
	pygame.draw.rect(screen, WHITE, (145,20,50,50))
	pygame.draw.rect(screen, WHITE, (205,20,50,50))
	pygame.draw.rect(screen, WHITE, (265,20,50,50))
	pygame.draw.rect(screen, WHITE, (325,20,50,50))
	pygame.draw.rect(screen, WHITE, (25,80,50,50))
	pygame.draw.rect(screen, WHITE, (85,80,50,50))
	pygame.draw.rect(screen, WHITE, (145,80,50,50))
	pygame.draw.rect(screen, WHITE, (205,80,50,50))
	pygame.draw.rect(screen, WHITE, (265,80,50,50))
	pygame.draw.rect(screen, WHITE, (325,80,50,50))
	pygame.draw.rect(screen, WHITE, (25,140,50,50))
	pygame.draw.rect(screen, WHITE, (85,140,50,50))
	pygame.draw.rect(screen, WHITE, (145,140,50,50))
	pygame.draw.rect(screen, WHITE, (205,140,50,50))
	pygame.draw.rect(screen, WHITE, (265,140,50,50))
	pygame.draw.rect(screen, WHITE, (325,140,50,50))
	pygame.draw.rect(screen, WHITE, (25,200,50,50))
	pygame.draw.rect(screen, WHITE, (85,200,50,50))
	pygame.draw.rect(screen, WHITE, (145,200,50,50))
	pygame.draw.rect(screen, WHITE, (205,200,50,50))
	pygame.draw.rect(screen, WHITE, (265,200,50,50))
	pygame.draw.rect(screen, WHITE, (325,200,50,50))
	pygame.draw.rect(screen, WHITE, (25,260,50,50))
	pygame.draw.rect(screen, WHITE, (85,260,50,50))
	pygame.draw.rect(screen, WHITE, (145,260,50,50))
	pygame.draw.rect(screen, WHITE, (205,260,50,50))
	pygame.draw.rect(screen, WHITE, (265,260,50,50))
	pygame.draw.rect(screen, WHITE, (325,260,50,50))
	pygame.draw.rect(screen, WHITE, (25,320,50,50))
	pygame.draw.rect(screen, WHITE, (85,320,50,50))
	pygame.draw.rect(screen, WHITE, (145,320,50,50))
	pygame.draw.rect(screen, WHITE, (205,320,50,50))
	pygame.draw.rect(screen, WHITE, (265,320,50,50))
	pygame.draw.rect(screen, WHITE, (325,320,50,50))
	pygame.draw.rect(screen, WHITE, (25,380,50,50))
	pygame.draw.rect(screen, WHITE, (85,380,50,50))
	pygame.draw.rect(screen, WHITE, (145,380,50,50))
	pygame.draw.rect(screen, WHITE, (205,380,50,50))
	pygame.draw.rect(screen, WHITE, (265,380,50,50))
	pygame.draw.rect(screen, WHITE, (325,380,50,50))

	pygame.draw.rect(screen, WHITE, (250,500,50,50))

	screen.blit(pic1, (picx,picy))

	if start:
		# picx += speedx
		picy += speedy


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (250 <= mouse_x <= 300) and (500 <= mouse_y <= 550):
					start = True

	pygame.display.flip()

	timer.tick(60)

pygame.quit()