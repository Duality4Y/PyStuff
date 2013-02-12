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
		
		self.screenwidth = screenwidth;
		self.screenheight = screenheight;
		
		self.xd = 0;
		self.yd = 0;
		self.mx = 0;
		self.my = 0;
		
		self.projectilex = self.x+radius;
		self.projectiley = self.y+radius;
		
		self.projectileStep = 10;
		
		self.fired = False;
	
	def friendly(self):
		#draw our guy; at new x,y; actually should return attributes, and not draw here.
		print "self.x, self.y: ", self.x,self.y;
		return (int(self.x), int(self.y));
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
		
		if xw > self.dx:
			self.dx+=self.accel;
		if xw < self.dx:
			self.dx-=self.accel;
		if yw > self.dy:
			self.dy+=self.accel;
		if yw < self.dy:
			self.dy-=self.accel;
		
		self.dx = round(self.dx,1);
		self.dy = round(self.dy,1);
		self.x += self.dx;
		self.y += self.dy;
		self.bounderyCheck();

class projectile(object):
	def __init__(self):
		#try:
		unit = self.projectileDirection();
		self.x = unit[0];
		self.y = unit[1];
		#except:
		#	self.x = 0;
		#	self.y = 0;
		self.projectilex = 0;
		self.projectiley = 0;
		self.mx = 0;
		self.my = 0;
		self.fired = False;
		
		
	def projectileFire(self, x,y):
		self.x,self.y = x,y;
		self.fired = True;
	
	def projectileReset(self):
		unit = self.projectileDirection();
		self.projectilex = unit[0]+self.x+radius;
		self.projectiley = unit[1]+self.y+radius;
		self.fired = False;
	
	def projectileBoundery(self):
		if player1.projectilex <= player1.fieldstartx+radius:
			self.projectileReset();
		elif player1.projectilex >= player1.screenwidth - player1.fieldstartx - player1.radius:
			self.projectileReset();
		
		if player1.projectiley <= player1.fieldstarty+radius:
			self.projectileReset();
		elif player1.projectiley >= player1.screenheight-player1.fieldstarty-player1.radius:
			self.projectileReset();
	
	def projectileDirection(self):
		#if self.fired:
		dx = self.mx - self.x;
		dy = self.my - self.y;
		length = (dx**2+dy**2)**0.5;
		unitx = dx/length;
		unity = dy/length;
		
		return (unitx,unity,length);
	def projectileMove(self):
		try:
			print "unitx,unity",self.projectileDirection();
			unit = self.projectileDirection();
			self.projectilex += unit[0]*self.projectileStep;
			self.projectiley += unit[1]*self.projectileStep;
		except:
			pass;
	
	def projectile(self):
		self.projectileBoundery();
		return self.projectilex,self.projectiley;

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

rect = fieldstartx,fieldstarty,fieldwidth,fieldheight=(100,100, 600, 400);
color = (255,255,255);
radius = 10;
positionx = rect[0]+fieldwidth/2;
positiony = rect[1]+fieldheight/2;
positionStep = 10;

running = 1;

player1 = Friendly(width, height, (positionx, positiony), fieldstartx, fieldstarty, radius);
pygame.time.set_timer(USEREVENT+1, 20);
projectile1 = projectile();
while running:
	for event in pygame.event.get():
		if event.type == USEREVENT+1:
			player1.control();
		if event.type == MOUSEBUTTONDOWN:
			print 'mouse event', event;
			#left mouse button clicked:
			if event.button == 1:
				print 'mouse button 1 pressed';
				(mousex,mousey) = pygame.mouse.get_pos();
				projectile1.projectileFire(player1.x, player1.y);
				projectile1.mx = mousex;
				projectile1.my = mousey;
				projectile1.fired = True;
		if event.type == QUIT:
			running = 0;
		#print 'event: ', str(event);
	print "fpsTick: ", fpsTick; 
	print "position: ", player1.x, player1.y;
	
	screen.fill((0,0,0));
	pygame.draw.rect(screen, color,rect , 1);
	
	pygame.draw.circle(screen, color, player1.friendly(), radius, 1);
	
	pygame.draw.circle(screen, color, projectile1.projectile(), radius/5, 1);
	projectile1.projectileMove();
	
	pygame.display.flip();
	#fpsClock.tick(fpsTick);

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
