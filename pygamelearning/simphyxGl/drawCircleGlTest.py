import pygame
from pygame.locals import *

import sys; sys.path.insert(0,"..")
import pygl2d

from math import *
width,height = 640,480;
pygl2d.window.init([width,height])

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #return
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();
                #return
    pygl2d.window.begin_draw();
    pygl2d.draw.rect([0,0,width,height],[255,255,255])
    pygl2d.draw.rect([100,100,200,200],[0,0,0])
    pygl2d.draw.circle([400,400],10,[0,0,0])
    pygl2d.window.end_draw();