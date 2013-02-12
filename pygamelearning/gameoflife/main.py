'''
Created on Nov 27, 2012

@author: duality
'''

import pygame
import random
from time import sleep
from pygame.locals import *

pygame.init();
size = width,height = 200,200;
flags = DOUBLEBUF;
screen = pygame.display.set_mode((size),flags);

white = (255,255,255);

lifeList = 10*[range(0,10)];
for row in lifeList:
    for thing in row:
        row[thing] = random.randint(0,1);
    print str(row);


def checkUpper():
    if y > 0:
        return lifeList[y-1][x];
    return 0;
def checkLower():
    if y < 10:
        return lifeList[y+1][x];
    return 0;
def checkLeft():
    if x > 0:
        return lifeList[y][x-1];
    return 0;
def checkRight():
    if x < 10:
        return lifeList[y][x+1];
    return 0;
def checkUpRightCorner():
    if x < 10 and y > 0:
        return lifeList[y-1][x+1];
    return 0;
def checkUpLeftCorner():
    if x > 0 and y > 0:
        return lifeList[y-1][x-1];
    return 0;
def checkLowRightCorner():
    if x < 10 and y < 10:
        return lifeList[y+1][x+1];
    return 0;
def checkLowLeftCorner():
    if x > 0 and y < 10:
        return lifeList[y+1][x-1];
    return 0;

if __name__ == '__main__':
    running = 1;
    point = 0;
    r = 10
    x = 0;
    y = 0;
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0;
        try:
            neightbours = checkUpper()+checkLower()+checkLeft()+checkRight()+checkUpRightCorner()+checkUpLeftCorner()+checkLowRightCorner()+checkLowLeftCorner();
        except:
            pass;
        if not x%10:
            pygame.draw.circle(screen,(100,100,100),(x+r,y+r),r,1);
        if x == width/(r+r):
            pygame.display.flip();
            x = 0;
            if y > height:
                #screen.fill(white);
                y = 0;
            else:
                y += r;
        x += 1;
        sleep(0.10);
        print "x,y,x%10,ax,ay>> ",x,y,x%10;