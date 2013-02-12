#!/bin/env python

import wireframe
import pygame, math

width, height = 400, 300
background = (10,10,50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Wireframe Display')

class ProjectionViewer:
    def __init__(self, width, height):
        self.models = {}
        self.width = width
        self.height = height
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4

    def addModel(self, name, wireframe):
        self.models[name] = wireframe

    def display(self, screen):
        """ Draw the nodes and/or the edges of a wireframe onto a screen """
            
        for model in self.models.values():
            if self.displayEdges:
                for edge in model.edges:
                    pygame.draw.aaline(screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)

            if self.displayNodes:
                for node in model.nodes:
                    pygame.draw.circle(screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)

    def translate(self, model, axis, d):
        """ Add constant 'd' to the coordinate 'axis' of each node of a model """
        
        if axis in ['x', 'y', 'z']:
            for node in self.models[model].nodes:
                setattr(node, axis, getattr(node, axis) + d)

    def scale(self, model, scale):
        """ Scale the model from the centre of the screen """

        centre_x = self.width/2
        centre_y = self.height/2

        for node in self.models[model].nodes:
            node.x = centre_x + scale*(node.x - centre_x)
            node.y = centre_y + scale*(node.y - centre_y)
            node.z *= scale

    def rotateX(self, model, radians):
        (cx,cy,cz) = self.models[model].findCentre()
        
        for node in self.models[model].nodes:
            y      = node.y - cy
            z      = node.z - cz
            d      = math.hypot(y, z)
            theta  = math.atan2(y, z) + radians
            node.z = cz + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

    def rotateY(self, model, radians):
        (cx,cy,cz) = self.models[model].findCentre()
        
        for node in self.models[model].nodes:
            x      = node.x - cx
            z      = node.z - cz
            d      = math.hypot(x, z)
            theta  = math.atan2(x, z) + radians
            node.z = cz + d * math.cos(theta)
            node.x = cx + d * math.sin(theta)

    def rotateZ(self, model, radians):
        (cx,cy,cz) = self.models[model].findCentre()
        
        for node in self.models[model].nodes:
            x      = node.x - cx
            y      = node.y - cy
            d      = math.hypot(y, x)
            theta  = math.atan2(y, x) + radians
            node.x = cx + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

cube = wireframe.Wireframe()
cube.addNodes([(x,y,z) for x in (50,250) for y in (50,250) for z in (50,250)])
cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])

pv = ProjectionViewer(width, height)
pv.addModel('cube', cube)

key_to_function = {
    pygame.K_LEFT:   (lambda x, obj: x.translate(obj, 'x', -10)),
    pygame.K_RIGHT:  (lambda x, obj: x.translate(obj, 'x',  10)),
    pygame.K_DOWN:   (lambda x, obj: x.translate(obj, 'y',  10)),
    pygame.K_UP:     (lambda x, obj: x.translate(obj, 'y', -10)),
    pygame.K_EQUALS: (lambda x, obj: x.scale(obj, 1.25)),
    pygame.K_MINUS:  (lambda x, obj: x.scale(obj, 0.8)),
    pygame.K_q:      (lambda x, obj: x.rotateX(obj,  0.1)),
    pygame.K_w:      (lambda x, obj: x.rotateX(obj, -0.1)),
    pygame.K_a:      (lambda x, obj: x.rotateY(obj,  0.1)),
    pygame.K_s:      (lambda x, obj: x.rotateY(obj, -0.1)),
    pygame.K_z:      (lambda x, obj: x.rotateZ(obj,  0.1)),
    pygame.K_x:      (lambda x, obj: x.rotateZ(obj, -0.1))
    }

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in key_to_function:
                key_to_function[event.key](pv, 'cube')

    screen.fill(background)
    pv.display(screen)  
    pygame.display.flip()