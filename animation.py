import pygame

pygame.init()

screen = pygame.display.set_mode([500,400])

running = True
start = False

GREY = (150,150,150)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

picx = 0
picy = 0

speedx = 1
speedy = 1

pic = pygame.image.load("logo.png")
pic1 = pygame.transform.scale(pic, (50,50))

timer = pygame.time.Clock()

while running:
	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (100,100,50,50))
	screen.blit(pic1, (picx,picy))

	if start:
		picx += speedx
		picy += speedy


		if picx <= 0 or picx + pic.get_width() >= 960:
			speedx = -speedx
		if picy <= 0 or picy + pic.get_height() >= 860:
			speedy = -speedy


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (100 <= mouse_x <= 150) and (100 <= mouse_y <= 150):
					start = True

	pygame.display.flip()

	timer.tick(120)

pygame.quit()