'''
Created on Oct 28, 2012

@author: duality
'''
#been playing around again with pygame is fun you know :)!!!
import pygame
import math
from pygame.locals import *
import sys
import random

pygame.init();
size = width,height = 1280,700;
border = 10,50,width-20,height-60;
flags = DOUBLEBUF|HWACCEL|HWSURFACE|FULLSCREEN;
screen = pygame.display.set_mode((size))#, flags);

white = (255,255,255);
black = (0,0,0);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);

running = 1;

leftMouseState = rightMouseState = 0;
drawLine = 0;
drawCircle1 = 0;
drawCircle2 = 0;

class Player(object):
    def __init__(self,startPosition,border,speed,accel,colour,radius):
        self.x = startPosition[0];
        self.y = startPosition[1];
        self.r = radius;
        self.border = border;
        self.colour = colour;
        
        self.v =  speed;
        self.dx = 0;
        self.dy = 0;
        self.accel = accel;
        self.xw = self.yw = 0;
        
        self.CD = collisionDetect();
        
    def controls(self,keylist,keys):
        xw = yw = 0;
        
        if keys[keylist[0]] == 1:
            xw = -self.v;
        if keys[keylist[1]] == 1:
            xw = self.v;
        if keys[keylist[2]] == 1:
            yw = -self.v;
        if keys[keylist[3]] == 1:
            yw = self.v;
        
        if xw > self.dx:
            self.dx += self.accel;
        if xw < self.dx:
            self.dx -= self.accel;
        if yw > self.dy:
            self.dy += self.accel;
        if yw < self.dy:
            self.dy -= self.accel;
        
        self.dx = round(self.dx,1);
        self.dy = round(self.dy,1);
        self.x += round(self.dx);
        self.y += round(self.dy);
        
        #check here if we hit something.\
        self.x,self.y = self.CD.boundery((self.x,self.y),self.r,self.border);
            
    def player(self):
        #return a tuple of the position.
        return (int(self.x),int(self.y));
    def hitPlayer(self,pos,r):
        dX = pos[0]-self.x;
        dY = pos[1]-self.y;
        length = math.sqrt((dY**2)+(dX**2));
        #print "length: ", length;
        if length <= self.r+r:
            #self.accel -= 0.01;
            self.dx *= -1;
            self.dy *= -1;
            self.dx+self.v+self.r;
            self.dy+self.v+self.r;
            return True;
        
    def followPlayer(self, pos):
        vX = self.x-pos[0];
        vY = self.y-pos[1];
        pass;
    def reset(self):
        #self.dx = self.dy = 0;
        self.xw = self.yw = self.dx = self.dy = 0;
    def rect(self):
        return self.x-self.r-1,self.y-self.r-1,2*self.r+1,2*self.r+1;
    def FollowPlayer(self,pos):
        #pygame.draw.line(screen,green,(self.x,self.y),pos,1);
        #print "vector: ",self.x-pos[0],self.y-pos[1];
        self.xw = self.yw = 0;
        
        vectX = self.x-pos[0];
        vectY = self.y-pos[1];
        length = math.sqrt((vectY**2)+(vectX**2));
        
        #K_LEFT,K_RIGHT,K_UP,K_DOWN
        if vectX > 0:
            self.xw = -self.v;
        if vectX < 0:
            self.xw = self.v;
        if vectY > 0:
            self.yw = -self.v;
        if vectY < 0:
            self.yw = self.v;
        
        if self.xw > self.dx:
            self.dx += self.accel;
        if self.xw < self.dx:
            self.dx -= self.accel;
        if self.yw > self.dy:
            self.dy += self.accel;
        if self.yw < self.dy:
            self.dy -= self.accel;
            
        #self.dx = round(self.dx,1);
        #self.dy = round(self.dy,1);
        self.x += self.dx;
        self.y += self.dy;
        #self.x,self.y = self.CD.boundery((self.x,self.y),self.r,self.border);
        #self.x, self.y = self.CD.infiniteBoundery((self.x,self.y),self.r,self.border);
            #self.reset();

class collisionDetect(object):
    def __init__(self):
        pass;
    
    def boundery(self,pos,r,bound):
        position = list(pos)
        if position[0] <= bound[0]+r:
            position[0] = bound[0]+r;
        if position[0] >= bound[2]+bound[0]-r:
            position[0] = bound[2]+bound[0]-r;
        if position[1] <= bound[1]+r:
            position[1] = bound[1]+r;
        if position[1] >= bound[3]+bound[1]-r:
            position[1] = bound[3]+bound[1]-r;
        return position[0],position[1];
    
    def infiniteBoundery(self,pos,r,bound):
        posX = pos[0];
        posY = pos[1];
        bounderyX = bound[0];
        bounderyY = bound[1];
        bounderyWidth = bound[2];
        bounderyHeight = bound[3];
        
        if posX-r < bounderyX:
            posX = bounderyWidth+bounderyX-r;
        if posX+r > bounderyX+bounderyWidth:
            posX = bounderyX+r;
        if posY+r > bounderyY+bounderyHeight:
            posY = bounderyY+r;
        if posY-r < bounderyY:
            posY = bounderyHeight+bounderyY-r;
        return posX,posY;
    def hitBoundery(self,pos,r,bound):
        position = list(pos)
        if position[0] <= bound[0]+r:
            return True;
        if position[0] >= bound[2]+bound[0]-r:
            return True;
        if position[1] <= bound[1]+r:
            return True;
        if position[1] >= bound[3]+bound[1]-r:
            return True;
        return False;
        #return position[0],position[1];

def processPlayers(enableControl):
    #draw the players.
    #do calculations on the individuals.
    #screen.fill(white);
    for i in xrange(1,len(my_players),1):
        first = my_players[0];
        second = my_players[i];
        if enableControl:
            if leftMouseState:
                first.x,first.y = pygame.mouse.get_pos();
                first.reset();
            if rightMouseState:
                second.x,second.y = pygame.mouse.get_pos();
                second.reset();
            if not leftMouseState:
                first.FollowPlayer(second.player());
            if not rightMouseState:
                second.FollowPlayer(first.player());
            if drawLine:
                pygame.draw.line(screen,second.colour,first.player(),second.player(),1);
            if drawCircle1:
                #pygame.draw.circle(screen,red,first.player(),first.r,0);
                pygame.draw.circle(screen,red,first.player(),first.r,1);
            if drawCircle2:
                pygame.draw.circle(screen,second.colour,second.player(),second.r,0);
        pygame.draw.circle(screen,second.colour,second.player(),second.r,1);
        #pygame.draw.line(screen,second.colour,first.player(),second.player(),1);
        first.FollowPlayer(second.player());
        second.FollowPlayer(first.player());
        #first.hitPlayer(second.player(),second.r);
        #second.hitPlayer(first.player(),first.r);


def Quit():
    running = 0;
    pygame.quit();
    sys.exit();

my_players = [];
number_of_players = 1000;

for p in range(number_of_players):
    x = random.randint(100,width-100);
    y = random.randint(100,height-100);
    speed = random.randint(20,50);
    accel = random.uniform(0.1,0.01);
    size = 3#random.randint(8,16);
    red = random.randint(1,255);
    green = random.randint(1,255);
    blue = random.randint(1,255);
    colour = black#(red,green,blue)
    my_players.append(Player((x,y),border,speed,accel,colour,size));
    
my_players[0].accel = 0.0001;
my_players[0].speed = 1;

keylist = [K_LEFT,K_RIGHT,K_UP,K_DOWN,
           K_a, K_d, K_w, K_s];

#pygame.time.set_timer(USEREVENT+1, 40);
pygame.time.set_timer(USEREVENT+2, 80);

screen.fill(white);
pygame.display.flip();
screen.set_alpha(None);

if __name__ == '__main__':
    while running:
        screen.fill(white); 
        #def eventHandling():
        for event in pygame.event.get():
            if event.type == QUIT:
                Quit();
            if event.type == KEYDOWN:
                if event.key == K_l:
                    if drawLine :
                        drawLine = 0;
                    else:
                        drawLine = 1;
                if event.key == K_1:
                    if drawCircle1:
                        drawCircle1 = 0;
                    else:
                        drawCircle1 = 1;
                if event.key == K_2:
                    if drawCircle2:
                        drawCircle2 = 0;
                    else:
                        drawCircle2 = 1;
                if event.key == K_q:
                    Quit();
            #if event.type == KEYUP:
            #    if event.key == K_l:
            #        drawLine = 0;
            #    if event.key == K_1:
            #        drawCircle1 = 0;
            #    if event.key == K_2:
            #        drawCircle2 = 0;
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    leftMouseState = 1;
                if event.button == 3:
                    rightMouseState = 1;
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    leftMouseState = 0;
                if event.button == 3:
                    rightMouseState = 0;
            #if event.type == USEREVENT+1:
                #keys = pygame.key.get_pressed();
                #player1.controls(keylist,keys);
                #player2.controls(keylist[4:],keys);
            #if event.type == USEREVENT+2:
        processPlayers(True);
        #return True;
        #eventHandling();
        pygame.draw.rect(screen,black,border,1);
        pygame.display.flip();