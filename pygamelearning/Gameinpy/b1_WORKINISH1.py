import math;
import pygame;
from pygame.locals import *;
import sys;

class Item(object):
    def __init__(self, position,direction,radius):
        self.px = position[0];
        self.py = position[1];
        self.dx = direction[0];
        self.dy = direction[1];
        self.v = math.sqrt(self.dx*self.dx+self.dy*self.dy);
        self.r = radius;

class Obstacle(object):
    def shipCollision(self, position,direction):
        return None;
    def boltCollision(self, position,direction):
        return None;

class Wall(Obstacle):
    def __init__(self,begin,end):
        self.px = begin[0];
        self.py = begin[1];
        self.dx = end[0]-begin[0];
        self.dy = end[1]-begin[1];
    def shipCollision(self, item):
        pass;
    def boltCollison(self, position,direction):
        pass;

class Player(object):
    def __init__(self, position,fieldstartx, fieldstarty, fieldwidth, fieldheight, radius):
        self.x = position[0];
        self.y = position[1];
        self.r = radius;
        self.v = 20;
        self.dx = 0;
        self.dy = 0;
        
        self.fieldstartx = fieldstartx;
        self.fieldstarty = fieldstarty;
        self.fieldHeight = fieldheight;
        self.fieldWidth = fieldwidth;
        
    def checkControls(self,keyleft,keyright,keyup,keydown):
        keys = pygame.key.get_pressed();
        
        xw = 0;
        yw = 0;
        
        accel = 1;
        
        if keys[keyleft] == 1:
            xw = -self.v;
        if keys[keyright] == 1:
            xw = self.v;
        if keys[keyup] == 1:
            yw = -self.v;
        if keys[keydown] == 1:
            yw = self.v;
        
        if xw > self.dx:
            self.dx+=accel;
        if xw < self.dx:
            self.dx -= accel;
        if yw > self.dy:
            self.dy+=accel;
        if yw < self.dy:
            self.dy-=accel;
        
        self.dx = round(self.dx,1);
        self.dy = round(self.dy, 1);
        self.x += self.dx;
        self.y += self.dy;
        self.x,self.y = self.bounderyCheck(self.x,self.y,self.r);
    
    def bounderyCheck(self,x,y,r):
        if x <= self.fieldstartx+r:
            x = self.fieldstartx+r;
        elif x >= self.fieldWidth+self.fieldstartx-r:
            x = self.fieldWidth+self.fieldstartx-r;
        if y <= self.fieldstarty+r:
            y = self.fieldstarty+r;
        elif y >= self.fieldHeight+self.fieldstarty-r:
            y = self.fieldHeight+self.fieldstarty-r;
        return x,y;
        
    def player(self):
        return (int(self.x), int(self.y));
    
    
pygame.init();
size = width, height = 800,600;
screen = pygame.display.set_mode((size), DOUBLEBUF);
#fpsClock = pygame.time.Clock();
#fpsTick = 30;
#Tick = 1;
white = (255,255,255);
black = (0,0,0);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);

pygame.time.set_timer(USEREVENT+1, 20);

field = fieldstartx,fieldstarty, fieldwidth, fieldheight = (100,100,600,400)

shipSize = 10;
shipX = fieldstartx+fieldwidth/2;
shipY = fieldstarty+fieldheight/2;

Player1 = Player((shipX,shipY), fieldstartx, fieldstarty, fieldwidth, fieldheight, shipSize)
Player2 = Player((shipX+20,shipY+20), fieldstartx, fieldstarty, fieldwidth, fieldheight, shipSize)
Player3 = Player((shipX-20,shipY-20), fieldstartx, fieldstarty, fieldwidth, fieldheight, shipSize)


running = 1;
while running:
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            Player1.checkControls(K_LEFT,K_RIGHT,K_UP,K_DOWN);
            Player2.checkControls(K_a, K_d, K_w, K_s);
            Player3.checkControls(K_f, K_h, K_t, K_g);
        if event.type == QUIT:
            running = 0;
            pygame.quit();
            sys.exit();
    screen.lock();
    screen.fill(black);
    pygame.draw.rect(screen,white,field,1);
    pygame.draw.circle(screen, red, Player1.player(), shipSize, 0);
    pygame.draw.circle(screen, green, Player2.player(), shipSize, 0);
    pygame.draw.circle(screen, blue, Player3.player(), shipSize, );
    
    
    dx = Player1.player()[0]-Player2.player()[0];
    dy = Player1.player()[1]-Player2.player()[1];
    print "dx, dy", dx,dy;
    near = round(math.sqrt((dx*dx)+(dy*dy)),1);
    print "near: ", near;
    if near<=(shipSize*2) or near == 0:
        print "bam";
    
    pygame.draw.line(screen, red, Player1.player(),Player2.player(), 1)
    pygame.draw.line(screen, green, Player2.player(),Player3.player(), 1)
    pygame.draw.line(screen, blue, Player1.player(),Player3.player(), 1)
    
    screen.unlock();
    pygame.display.flip();
    #fpsClock.tick(fpsTick);