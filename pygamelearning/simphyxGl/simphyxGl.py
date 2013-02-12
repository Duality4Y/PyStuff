import random
import numpy
import pygame
import PyParticles

import sys; sys.path.insert(0,"..")
import pygl2d

(width, height) = (400, 400)
size = [width,height]
#screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Star formation')
pygl2d.window.init(size);

universe = PyParticles.Environment((width, height))
universe.colour = (0,0,0)
universe.addFunctions(['move', 'attract', 'combine'])

def calculateRadius(mass):
    return 0.5 * mass ** (0.5)

for p in range(40):
    particle_mass = random.randint(1,4)
    particle_size = calculateRadius(particle_mass)
    universe.addParticles(mass=particle_mass, size=particle_size, speed=0, colour=(255,255,255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygl2d.window.begin_draw();
    pygl2d.draw.rect([0,0,width,height],[0,0,0])
    #screen.fill(universe.colour)
    universe.update()
    
    particles_to_remove = []
    for p in universe.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = calculateRadius(p.mass)
            del p.__dict__['collide_with']

        if p.size < 2:
            pygl2d.draw.rect([p.x,p.y,2,2],p.colour)
            #pygame.draw.rect(screen, p.colour, (int(p.x), int(p.y), 2, 2))
        else:
            pygl2d.draw.circle([p.x,p.y],p.size,p.colour);
            #pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), int(p.size), 0)
    
    pygl2d.window.end_draw();
    for p in particles_to_remove:
        if p in universe.particles:
            universe.particles.remove(p)
    #pygame.display.flip()
