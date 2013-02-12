import pygame
from pygame.locals import *
import random
import math

running = True;
(height, width) = (400,400);
screen = pygame.display.set_mode((width, height), DOUBLEBUF);
clock = pygame.time.Clock();
Tick=0;
TickStep = 2;

class Particle:
	def __init__(self, (x,y), size, mass=1):
		self.x = x;
		self.y = y;
		self.size = size;
		self.mass= mass;
		self.color = (255,255,255);
		self.speed = 0;
		self.angle = 0;
		self.elasticity = 0.9;
	def move(self):
		self.x += math.sin(self.angle)*self.speed; #with math.sine(self.angle) calulate the x position. times the speed (at which rate it moves);
		self.y -= math.cos(self.angle)*self.speed; #minus because of the inverted y axis. cossine beccause it's 90 degrea ontop of x axis.
	def infiniteField(self):
		
		if self.x > width+self.size+1:
			self.x = self.size;
		elif self.x < -self.size-1:
			self.x = width-self.size;
		
		if self.y > height+self.size+1:
			self.y = self.size;
		elif self.y < -self.size-1:
			self.y = height-self.size;
		
	def boundery(self):
		"""noramly a particle would leave under the same angle as 
			it arrives, but i'll try this :).
			apperently on the x axis inverting the angle works, but not for the y,
			i think this is a cos aka a verticale axis."""
		
		if self.x > width-self.size:
			self.x = 2*(width - self.size)-self.x;
			self.angle = -self.angle; #invert angle on x axis.
			self.speed *= self.elasticity;
		elif self.x < self.size:
			self.x = 2*self.size-self.x
			self.angle = -self.angle;
			self.speed *= self.elasticity;
				
		if self.y > height-self.size:
			self.y = 2*(width - self.size) - self.y;
			self.angle = math.pi - self.angle; #invert on y axis plus a pi turned halve a circle). 2pi == full circle (makes sense now);
			self.speed *= self.elasticity;
		elif self.y < self.size:
			self.y = 2*self.size - self.y;
			self.angle = math.pi - self.angle;
			self.speed *= self.elasticity;
	
	def accelerate(self, vector):
		""" Change angle and speed by a given vector """
		(self.angle, self.speed) = addVectors((self.angle, self.speed), vector)
	
	def attract(self, other):
		"""" Change velocity based on gravatational attraction between two particle"""
		
		dx = (self.x - other.x)
		dy = (self.y - other.y)
		dist  = math.hypot(dx, dy)
		
		if dist < self.size + self.size:
			return True
		
		theta = math.atan2(dy, dx)
		force = 0.2 * self.mass * other.mass / dist**2
		self.accelerate((theta- 0.5 * math.pi, force/self.mass))
		other.accelerate((theta+ 0.5 * math.pi, force/other.mass))
		
	def position(self):
		pos = (self.x, self.y);
		return pos;
	def update(self):
		#self.boundery();
		self.move();
		self.infiniteField();

def collide(p1, p2):
	dx = p1.x - p2.x
	dy = p1.y - p2.y
	
	dist = math.hypot(dx, dy)
	if dist < p1.size + p2.size:
		angle = math.atan2(dy, dx) + 0.5 * math.pi
		total_mass = p1.mass + p2.mass
		
		(p1.angle, p1.speed) = addVectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass), (angle, 2*p2.speed*p2.mass/total_mass))
		(p2.angle, p2.speed) = addVectors((p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass), (angle+math.pi, 2*p1.speed*p1.mass/total_mass))
		elasticity = p1.elasticity * p2.elasticity
		p1.speed *= elasticity
		p2.speed *= elasticity
		
		overlap = 0.5*(p1.size + p2.size - dist+1)
		p1.x += math.sin(angle)*overlap
		p1.y -= math.cos(angle)*overlap
		p2.x -= math.sin(angle)*overlap
		p2.y += math.cos(angle)*overlap
def addVectors((angle1, length1), (angle2, length2)):
    """ Returns the sum of two vectors """
    
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle  = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

particles = [];
num_particles = 20;

for p in range(num_particles):
	size = random.randint(2, 10);
	particle = Particle((random.randint(size,width), random.randint(size,height)), size, random.randint(1,50))
	particle.speed = 0;
	particle.angle = 0;
	particles.append(particle);

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False;
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_MINUS:
				Tick+=TickStep;
			elif event.key == pygame.K_EQUALS:
				Tick-=TickStep;
	print "Tick: ", Tick;
	screen.fill((0,0,0));

	for i, particle in enumerate(particles):
		try:
			pygame.draw.circle(screen, particle.color, (int(particle.x),int(particle.y)), particle.size, 1);
		except ValueError:
			pass;
		print i," :particle.x: ", particle.x;
		print i," :particle.y: ", particle.y;
		for particle2 in particles[i+1:]:
			#collide(particle, particle2);
			collide(particle, particle2);
			particle.attract(particle2);
			particle.update();
	clock.tick(Tick);
	pygame.display.flip();
