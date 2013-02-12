import sys, os, math, pygame, pygame.mixer;
from pygame.locals import *;
import random;


black = 0,0,0;
white = 255,255,255;
red = 255,0,0;
green = 0,255,0;
blue = 0,0,255;

colors = [black,red,green,blue];

size = width, height = 600,400;
screen = pygame.display.set_mode(size);
clock = pygame.time.Clock();
pygame.display.set_caption('frist classy');

fps_limit = 60;
run_me = 1;

class Circle(object):
	def __init__(self, (x,y), size, color=(255,255,255), width=1):
		self.x = x;
		self.y = y;
		self.size = size;
		self.color = color;
		self.width = width;
	def display(self):
		pygame.draw.circle(screen, self.color, (self.x,self.y), self.size, self.width);

num_circles = 10;
circles = [];

for i in range(num_circles):
	size = random.randint(10,20);
	x = random.randint(size, width-size);
	y = random.randint(size, height-size);
	color = random.choice(colors);
	circles.append(Circle((x,y), size, color));

while run_me:
	clock.tick(fps_limit);
	for event in pygame.event.get():
		if event.type == QUIT:
			run_me = 0;
	
	screen.lock();
	screen.fill(white);
	for circle in circles:
		circle.display();
	screen.unlock();
	
	pygame.display.flip();
pygame.quit();
sys.exit();