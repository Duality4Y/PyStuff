import pygame, sys
from pygame.locals import *

windowSize = 800,600;
screen = pygame.display.set_mode((windowSize),DOUBLEBUF);
running = True;

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit();
	#screen.fill((0,0,0));
	for x in range(1,20,1/10):
		y = (2**x)/4;
		pygame.draw.circle(screen,(255,255,255),(x,y),1,0);
		pygame.display.flip();
		print x;
