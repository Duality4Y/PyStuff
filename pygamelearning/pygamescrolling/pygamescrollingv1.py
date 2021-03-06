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
size = width,height = 700,700;
border = 10,50,680,640;
flags = DOUBLEBUF;
screen = pygame.display.set_mode((size), flags);

white = (255,255,255);
black = (0,0,0);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);

running = 1;

keylist = [K_LEFT,K_RIGHT,K_UP,K_DOWN,
           K_a, K_d, K_w, K_s];

class Player(object):
    def __init__(self,startPosition,border,speed,accel,radius):
        self.x = startPosition[0];
        self.y = startPosition[1];
        self.r = radius;
        self.border = border;
        
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
            self.dx *= -1;
            self.dy *= -1;
            return True;
        
    def followPlayer(self, pos):
        vX = self.x-pos[0];
        vY = self.y-pos[1];
        pass;
    def reset(self):
        self.xw = self.yw = self.dx = self.dy = 0;
    def _followPlayer(self,pos):
        #pygame.draw.line(screen,green,(self.x,self.y),pos,1);
        #print "vector: ",self.x-pos[0],self.y-pos[1];
        self.xw = self.yw = 0;
        
        vectX = self.x-pos[0];
        vectY = self.y-pos[1];
        
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
        self.x,self.y = self.CD.infiniteBoundery((self.x,self.y),self.r,self.border);

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

def processPlayers():
    for i in xrange(0,number_of_players,2):
        first = my_players[i];
        for j in xrange(1,number_of_players,2):
            second = my_players[j];
            pygame.draw.line(screen,blue,first.player(),second.player(),1);
            first._followPlayer(second.player());
            second._followPlayer(first.player());
    

pygame.time.set_timer(USEREVENT+1, 30);
pygame.time.set_timer(USEREVENT+2, 10);

#player1 = Player((200,200),border,1000,0.5,10);
#player4 = Player((100,100),border,10,0.5,10);

#player2 = Player((300,300),border,5,0.5,10);
#player3 = Player((width/2,height/2),border,10,0.5,10);

my_players = [];
number_of_players = 2;

for p in range(number_of_players):
    x = random.randint(0,700);
    y = random.randint(0,700);
    speed = random.randint(1,20);
    accel = random.uniform(0.1,1);
    size = 10;
    my_players.append(Player((x,y),border,speed,accel,size));
    pass;

leftMouseState = rightMouseState = 0;
      
if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0;
                pygame.quit();
                sys.exit();
            if event.type == MOUSEBUTTONDOWN:
                #print event.button
                if event.button == 1:
                    leftMouseState = 1;
                if event.button == 3:
                    rightMouseState = 1;
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    leftMouseState = 0;
                if event.button == 3:
                    rightMouseState = 0;
            if event.type == USEREVENT+1:
                keys = pygame.key.get_pressed();
                #player1.controls(keylist,keys);
                #player2.controls(keylist[4:],keys);
            if event.type == USEREVENT+2:
                screen.fill(white);
                processPlayers();
                #if not leftMouseState:
                #    player3._followPlayer(player2.player());
                #    pass;
                #elif leftMouseState:
                #    player3.reset();
                #if not rightMouseState:
                #    player4._followPlayer(player1.player());
                #    pass;
                #elif rightMouseState:
                #    player4.reset();
                #    pass;
                #player2._followPlayer(player3.player());
                #player1._followPlayer(player4.player());
                #player2.hitPlayer(player3.player(),player3.r);
                #player3.hitPlayer(player2.player(),player2.r);
                pass;
        
        #pygame.draw.circle(screen,black,player1.player(),player1.r,1);
        #pygame.draw.circle(screen,red,player2.player(),player2.r,1);
        #pygame.draw.circle(screen,green,player3.player(),player3.r,1);
        #pygame.draw.circle(screen,blue,player4.player(),player4.r,1);
        #pygame.draw.line(screen,black,player1.player(),player4.player(),1);
        #pygame.draw.line(screen,green,player2.player(),player3.player(),1);
        pygame.draw.rect(screen,black,border,1);
        for player in my_players:
            pygame.draw.circle(screen,black,player.player(),player.r,1);
        
        
        #if leftMouseState:
        #    player3.x,player3.y = pygame.mouse.get_pos();
        #if rightMouseState:
        #    player4.x,player4.y = pygame.mouse.get_pos();
        #if rightMouseState and leftMouseState:
        #    player3.x = player3.y = 100;
        #    player2.x = player2.y = 200;
        #    player4.x = player4.y = 150;
        #    player1.x = player1.y = 250;
        #    player1.reset();
        #    player2.reset();
        #    player3.reset();
        #    player4.reset();
        
        pygame.display.flip();