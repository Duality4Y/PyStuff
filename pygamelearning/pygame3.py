import math
import pygame
from pygame.locals import *

class Friendly(object):
	def __init__(self, screenwidth, screenheight, (positionx, positiony), fieldstartx, fieldstarty, radius):
		self.x = positionx;
		self.y = positiony;
		self.fieldstartx = fieldstartx;
		self.fieldstarty = fieldstarty;
		self.radius = radius;
		self.mass = 5;
		self.positionStep = 5;
		self.accel = 0.2;
		self.keyupstate = self.keydownstate = self.keyleftstate = self.keyrightstate = 0;
		self.screenwidth = screenwidth;
		self.screenheight = screenheight;
		
		self.xd = 0;
		self.yd = 0;
	
	def friendly(self):
		#draw our guy; at new x,y; actually should return attributes, and not draw here.
		return (self.x, self.y);
		#pygame.draw.circle(self.screen,self.color, (self.x,self.y),self.radius, 1);
	
	def bounderyCheck(self):
		if self.x <= self.fieldstartx+radius:
			self.x = self.fieldstartx+radius;
		elif self.x >= self.screenwidth - self.fieldstartx - self.radius:
			self.x = self.screenwidth - self.fieldstartx - self.radius;
		
		if self.y <= self.fieldstarty+radius:
			self.y = self.fieldstarty+radius;
		elif self.y >= self.screenheight-self.fieldstarty-self.radius:
			self.y = self.screenheight-self.fieldstarty-self.radius;
		
	def control(self):
		keys = pygame.key.get_pressed();
		
		xw = 0;
		yw = 0;
		
		if keys[K_LEFT] == 1:
			xw = -self.positionStep;
		if keys[K_RIGHT] == 1:
			xw = self.positionStep;
		if keys[K_UP] == 1:
			yw = -self.positionStep;
		if keys[K_DOWN] == 1:
			yw = self.positionStep;
		if xw > self.xd:
			self.xd+=self.accel;
		if xw < self.xd:
			self.xd-=self.accel;
		if yw > self.yd:
			self.yd+=self.accel;
		if yw < self.yd:
			self.yd-=self.accel;
		
		self.xd = round(self.xd,1);
		self.yd = round(self.yd,1);
		self.x += self.xd;
		self.y += self.yd;
		self.bounderyCheck();

class projectile(object):
	def __init__(self):
		self.projectileStep = 5;
	def projectileFire(self, event):
		pass;
		return True;
	def projectileDirection(self):
		pass;
	def projectileMove(self):
		directionPoint = pygame.mouse.get_pos();
		print "direction ", directionPoint;

class enemy(object):
	def __init__():
		pass;

pygame.init();
size = width, height = 800,600;
screen = pygame.display.set_mode((size));
fpsClock = pygame.time.Clock();
fpsTick = 24;
Tick = 1;

(mousex, mousey) = (2,2);

try:
	j = pygame.joystick.Joystick(0);
	j.init();
	print "enable joystick: ", j.get_name();
except pygame.error:
	print "no joystick found.";

rect = fieldstartx,fieldstarty,fieldwidth,fieldheight=(100,100, 600, 400);
color = (255,255,255);
radius = 10;
positionx = rect[0]+fieldwidth/2;
positiony = rect[1]+fieldheight/2;
positionStep = 10;

running = 1;

player1 = Friendly(width, height, (positionx, positiony), fieldstartx, fieldstarty, radius);
pygame.time.set_timer(USEREVENT+1, 20);

while running:
	for event in pygame.event.get():
		if event.type == USEREVENT+1:
			player1.control();
		if event.type == MOUSEBUTTONDOWN:
			print 'mouse event', event;
			#left mouse button clicked:
			if event.button == 1:
				print 'mouse button 1 pressed';
				running = 0;
		if event.type == QUIT:
			running = 0;
		#print 'event: ', str(event);
	
	print "fpsTick: ", fpsTick; 
	print "position: ", player1.x, player1.y;
	
	screen.fill((0,0,0));
	pygame.draw.rect(screen, color,rect , 1);
	pygame.draw.circle(screen, color, player1.friendly(), radius, 1);
	
	pygame.display.flip();
	fpsClock.tick(fpsTick);
	
	projectile().projectileMove();

pygame.quit();

"""
def _keep():
	if buttonState == 1:
		(mousex,mousey) = pygame.mouse.get_pos();
		print "mouse get: ", (mousex,mousey);
	try:
		#radius = round(math.sqrt((mousex**2+mousey**2)));
		p1 = 400 - mousex;
		p2 = 200 - mousey;
		radius = round(math.sqrt(p1**2+p2**2));
	except ValueError:
		radius = 2;
		print "radius to small";
	if radius<1:
		radius = 1;
	print "radius: ", radius;
	pygame.draw.circle(screen, color, (400,200), int(radius), 1);
"""
