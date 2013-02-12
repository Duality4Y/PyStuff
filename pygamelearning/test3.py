#! /usr/bin/env python
import pygame
y = 0;
x = 0;
diry = 1;
dirx = 1;
running = 1;
width = 800;
height = 600;
screen = pygame.display.set_mode((width, height));
linecolor = 255,0,0
bgcolor = 0,0,0

while running:
	event = pygame.event.poll();
	if event.type == pygame.QUIT:
		running = 0;
	screen.fill(bgcolor);
	
	pygame.draw.line(screen, linecolor, (0, y), (width-1, y));
	y += diry;
	if y == 0 or y== height-1: diry *=-1;
	
	pygame.draw.line(screen, linecolor, (x, 0), (x, height-1));
	x += dirx;
	if x ==0 or x==width-1: dirx *=-1;
	
	pygame.display.flip();
