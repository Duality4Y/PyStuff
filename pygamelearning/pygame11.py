import math
import pygame
from pygame.locals import *
import sys

class Item(object):
    def __init__(self, position, direction,radius):
        self.px = position[0];
        self.py = position[1];
        self.dx = direction[0];
        self.dy = direction[1];
        self.s = math.sqrt(self.dx*self.dx+self.dy*self.dy);
        self.r = radius;

class Obstacle(object):
    def shipCollision(self,position,direction):
        return None;
    def boltCollision(self,position,direction):
        return None;

class Wall(Obstacle):
    def __init__(self, begin, end):
        self.px = begin[0];
        self.py = begin[1];
        self.dx = end[0]-begin[0];
        self.dy = end[1]-begin[1];
    def shipCollision(self,item):
        divider = (self.dy*item.dx-item.dy*self.dx);
        itemU = (self.dx*(item.py-self.py)-self.dy*(item.px-self.px))/divider;
        selfU = (item.dx*(item.py-self.py)-item.dy*(item.px-self.px))/divider;
        if selfU < 0 or selfU > 1:
            return None;
        elif selfU > 0 and selfU < (self.r+self.s):
            pass;
                    
    def boltCollision(self,position,direction):
        return None;
        pass;

class Player(object):
    def __init__(self,  (x, y), fieldstartx,  fieldstarty,  fieldWidth,  fieldHeight,  radius):
        self.x = x;
        self.y = y;
        self.fieldstartx = fieldstartx;
        self.fieldstarty = fieldstarty;
        self.fieldWidth = fieldWidth;
        self.fieldHeight = fieldHeight;
        self.radius = radius;
        
        self.step = 5;
        self.accel = 0.1;
        self.xwanted = 0;
        self.ywanted = 0;
        self.dx = 0;
        self.dy = 0;
        
        self.bx = 0;
        self.by = 0;
        self.bStep = 10;
        self.bdx = 0;
        self.bdy = 0;
        
        self.mx =radius 0;
        self.my = 0;
        
    def checkControls(self):
        #check what keys pressed
        keys = pygame.key.get_pressed();
        
        xw = 0;
        yw = 0;
        
        if keys[K_LEFT] == 1:
            xw = -self.step;
        if keys[K_RIGHT] == 1:
            xw = self.step;
        if keys[K_UP] == 1:
            yw = -self.step;
        if keys[K_DOWN] == 1:
            yw = self.step;
        
        #per timer interupt we try to make speed 0 or full step giving a feeling of acceleration or deceleration. 
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
        #check boundery.
        self.x,self.y = self.bounderyCheck(self.x, self.y, self.radius);
            
    def bounderyCheck(self,x,y,_radius):
        if x <= self.fieldstartx+_radius:
            x = self.fieldstartx+_radius;
        elif x >= self.fieldWidth + self.fieldstartx - _radius:
            x = self.fieldWidth + self.fieldstartx - _radius;
        
        if y <= self.fieldstarty+_radius:
            y = self.fieldstarty+_radius;
        elif y >= self.fieldHeight+self.fieldstarty-_radius:
            y = self.fieldHeight+self.fieldstarty-_radius;
        
        return x,y;
        
    def player(self):
        return (int(self.x),int(self.y));
    
    def shoot(self):
        #get direction in which to shoot.
        print "mouse point: ",self.mx,",",self.my;
        print "pointing direction from ship: ",self.mx-self.x,self.my-self.y;
        
        try:
            self.bdx = self.mx - self.x;
            self.bdy = self.my - self.y;
            length = (self.bdx**2+self.bdy**2)**0.5;
            unitx = self.bdx/length;
            unity = self.bdy/length;
            print "self.bdx, selb.bdy", self.bdx, self.bdy;
            self.bx = self.x+unitx+self.radius;
            self.by = self.y+unity+self.radius;
        except:
            pass;
        return (unitx,unity,length);
    def bmove(self):
        unit = self.shoot();
        self.bx += unit[0]*self.bStep;
        self.by += unit[1]*self.bStep;
        self.bx,self.by = self.bounderyCheck(self.bx,self.by,self.radius/5)
    def checkHit(self):
        pass;
    def bullit(self):
        return (int(self.bx),int(self.by));
        

pygame.init();
width, height = 800, 600;
screen = pygame.display.set_mode((width, height));
fpsClock = pygame.time.Clock();
fpsTick = 30;
Tick = 1;

field = fieldstartx, fieldstarty, fieldwidth, fieldheight=(100, 100, 600, 400);
color = (255, 255, 255);
#ship radius for now: and start position. middle of the field.
radius = 10; #could be seen as size.
shipX = fieldstartx+fieldwidth/2;
shipY = fieldstarty+fieldheight/2;

running = 1;
shot = 0;
#set a time for polling checking whether i pushed a key.
pygame.time.set_timer(USEREVENT+1,  20);
player1 = Player((shipX, shipY),  fieldstartx, fieldstarty,  fieldwidth, fieldheight,radius);
while running:
    for event in pygame.event.get():
        #activate if enough time has passed and check.
        if event.type == USEREVENT+1:
            player1.checkControls();
        if event.type == MOUSEBUTTONDOWN:
            #if left mouse button is pressed.
            if event.button == 1:
                shot = 1;
                (mousex,mousey) = pygame.mouse.get_pos();
                #player1.shoot((mousex,mousey));
                (player1.mx,player1.my) = (mousex,mousey);
        if event.type == QUIT:
            running =0;
            pygame.quit();
            sys.exit();
    
    screen.fill((0,0,0));
    pygame.draw.rect(screen, color, field, 1);
    pygame.draw.circle(screen, color, player1.player(), radius, 1);
    #if shot == 1:
    pygame.draw.circle(screen, color, player1.bullit(), radius/5, 1);
    player1.bmove();
    pygame.display.flip();
    
    print "position: ", player1.x, player1.y;
    print "fpsTick: ",  fpsTick;
    fpsClock.tick(fpsTick);
    


