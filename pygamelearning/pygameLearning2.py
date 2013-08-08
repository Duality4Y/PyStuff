import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(False)

ship = pygame.image.load("ship5.png")
ship = pygame.transform.scale(ship,(100,100))
ship_top = screen.get_height()-ship.get_height()
ship_left = screen.get_width()/2-ship.get_width()/2
screen.blit(ship, (ship_left, ship_top))

shot  = pygame.image.load("bullet.png")
shoot_y = 0
shoot_x = 0

while True:
	clock.tick(60)
	screen.fill((0,0,0))
	x,y = pygame.mouse.get_pos()
	screen.blit(ship, (x-ship.get_width()/2, ship_top))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif event.type == MOUSEBUTTONDOWN and event.button == 1:
			print "event: ",event
			shoot_y = 500
			shoot_x = x
	if shoot_y > 0:
		screen.blit(shot,(shoot_x,shoot_y))
		shoot_y -= 10
	
	pygame.display.update()
