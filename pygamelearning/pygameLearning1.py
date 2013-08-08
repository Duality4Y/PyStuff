import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)

tux = pygame.image.load("linux performance tuning.banana-boy-tux-perso-2990.png")
tux2 = pygame.image.load("linux performance tuning.banana-boy-tux-perso-2990.png")
tux = pygame.transform.scale(tux,(100,100))
tux2 = pygame.transform.scale(tux,(100,100))

background = pygame.image.load("Moon-wallpaper.jpg")
background = pygame.transform.scale(background,size)

clock = pygame.time.Clock()

running = True

black = (0,0,0)



x = 0
y = 0
r = 0
mx, my = 0,0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			running = False
		if event.type == MOUSEBUTTONDOWN:
			r+= 10
			if r == 250:
				r = 0
			mx,my = pygame.mouse.get_pos()
		if event.type == KEYDOWN and event.key == K_SPACE:
			pygame.image.save(screen, "screenshot")
		
	screen.fill((r,0,0))
	screen.blit(background,(0,0))
	screen.blit(tux2,(mx-50,my-50))
	screen.blit(tux,(x,y))
	pygame.display.flip()
	x += 1
	y += 1
	clock.tick(60)
sys.exit(0)
