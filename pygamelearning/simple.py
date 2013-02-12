import pygame, sys
from pygame.locals import *

width, height = 600, 400;
screen = pygame.display.set_mode((width,height), DOUBLEBUF);
running = 1;

clock = pygame.time.Clock();
Tick=0;

def vector():
	pass;

class Particle:
	def __init__(self, (x,y) , size,  color=(0,0,0), mass=1, speed=2):
		self.size = size;
		self.posx = x;
		self.posy = y;
		self.mass = mass;
		self.speed = speed;
		self.color = color;
	def mass(self):
		pass;
	def particle(self):
		pass;
	def particlePos(self):
		return (int(self.posx), int(self.posy));
	def move(self):
		self.posx += ((self.posx+self.speed)**2-(self.posx+self.speed)**2)**0.5;
		self.posy -= ((self.posy+self.speed)**2-(self.posy+self.speed)**2)**0.5;
	def particleField(self, width, heigth):
		pass;

class vehicle:
	def __init__():
		pass;

pcolor = (255,255,255);
particle = Particle((100,100), 10, pcolor);
particle2 = Particle((200,200), 10, pcolor);

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit();
	screen.fill((0,0,0));
	pygame.draw.circle(screen, particle.color, particle.particlePos(), particle.size, 0);
	pygame.draw.circle(screen, particle2.color, particle2.particlePos(), particle2.size, 0);
	particle.move();
	particle2.move();
	pygame.display.flip();
	clock.tick(Tick);
