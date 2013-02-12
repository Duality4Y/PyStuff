import math

#-----------x , y , width, height;
obstacle1 =(130,130,20,80);
obstacle2 =[300,200,200,200];
#obstacle3 =[100,100,200,200];

obstaclelist = [obstacle1,obstacle2]#,obstacle3]

class Player(object):
    def __init__(self,position,fieldstartx,fieldstarty, fieldwidth,fieldheight,radius):
        self.x = position[0];
        self.y = position[1];
        self.r = radius;
        self.v = 10;
        self.dx = 0;
        self.dy = 0;
        
        self.hit = False;
        self.locHit = 0,0;
        
        self.FieldB = fieldstartx,fieldstarty,fieldwidth,fieldheight;
        self.CD = CollisionDetect();
        
        self.fieldstartx = fieldstartx;
        self.fieldstarty = fieldstarty;
        self.fieldwidth = fieldwidth;
        self.fieldheight = fieldheight;
        
    def checkControls(self,keylist,keys):
        xw = yw = 0;
        accel = 0.5;
        
        if keys[keylist[0]] == 1:
            xw = -self.v;
        if keys[keylist[1]] == 1:
            xw = self.v;
        if keys[keylist[2]] == 1:
            yw = -self.v;
        if keys[keylist[3]] == 1:
            yw = self.v;
        
        if xw > self.dx:
            self.dx+=accel;
        if xw < self.dx:
            self.dx -= accel;
        if yw > self.dy:
            self.dy+=accel;
        if yw < self.dy:
            self.dy -= accel;
        self.dx = round(self.dx,1);
        self.dy = round(self.dy,1);
        self.x += self.dx;
        self.y += self.dy;
        
        
        self.x,self.y = self.CD.ObstacleHit((self.x,self.y),obstacle1);
        self.x,self.y = self.CD.Boundery((self.x,self.y),self.r,self.FieldB);
        
            
    def player(self):
        #we return a tuple of the position the player is currently at.
        return (int(self.x), int(self.y));

class Projectile(object):
    def __init__(self,x,y,size,fieldstartx,fieldstarty,fieldwidth,fieldheight):
        self.x = x;
        self.y = y;
        self.r = size;
        #initial speed is 0
        self.v = 0;
        self.angle = 0;
        
        self.CD = CollisionDetect();
        self.hit = False;
        self.status = False;
        
        self.FieldB = fieldstartx,fieldstarty,fieldwidth,fieldheight;
    def projectile(self):
        self.move();
        return (int(self.x),int(self.y));
    def Shoot(self, x,y):
        dx = x-self.x;
        dy = y-self.y;
        self.v = 8;
        self.status = True
        self.angle = 0.5*math.pi+math.atan2(dy,dx);
    def projectileRemove(self):
        pass;
    def move(self):
        #calculate how much we have to add to x;
        self.x+=math.sin(self.angle)*self.v;
        self.y-=math.cos(self.angle)*self.v;
        self.x,self.y = self.CD.Boundery((self.x,self.y),self.r,self.FieldB);
        self.hit = self.CD.Hit((self.x,self.y),self.r,self.FieldB)
#"""
#check boundery, i think i go for two kinds for now, one that displaces gameobjects,
#so it won't go further then that, like the filled edge, can't go past it.
#and one that returns true if hit, false if not.
#for projectiles, i think it would be handy :)
#or when you hit enemy's.
#"""
class CollisionDetect(object):
    def __init__(self):
        pass;
#    """
#    pos/position is cordinate of the object to track. like ship or enemy.
#    bound and obstacle are the boundery of obstacle bounds. (squares).
#    looks like the way i got my collision detection, it works from 
#    the inside out, thus if i used the methods, Boundery and Hit
#    """
    #detect a hit and return position before goes over.
    def Boundery(self,pos,r,bound):
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
    #detect hit and return if hit or not.
    def Hit(self,position,r,obstacle):
        if position[0]<=obstacle[0]+r:
            return True;
        if position[0]>=obstacle[2]+obstacle[0]-r:
            return True;
        if position[1]<=obstacle[1]+r:
            return True;
        if position[1]>=obstacle[3]+obstacle[1]-r:
            return True;
        return False;
    
    def ObstacleHit(self,object1,object2):
        posx = object1[0];
        posy = object1[1];
        
        object2x = object2[0];
        object2y = object2[1];
        object2Width = object2[2];
        object2Height = object2[3];
        return posx,posy;

            
#    x = position[0];
#    y = position[1];
#    fieldstartx = bound[0];
#    fieldstarty = bound[1];
#    fieldwidth = bound[2];
#    fieldheight = bound[3];
#    """

#calculate distance between objects if you want lol..
#arguments must be tuples.
#could be used for collision detection between two points.
def getDistance(p1,p2):
    dx = p1[0] - p2[0];
    dy = p1[1] - p2[1];
    #calculating the delta x and y, meening, the diffrence between the two points x and y.
    #and use that to calculate the distance between, like with A^2+B^2 = C^2
    #and thus resulting in the distance between points.
    distance = round(math.sqrt((dx*dx)+(dy*dy)),0);
    return distance;

#could be used for drawing a directional line between two points, returns two tuples.
#first tuple is starting point, second tuple is end point.
def DirectionLine(p1,dx,dy):
    p1 = list(p1);
    p1x = p1[0];
    p1y = p1[1];
    return (p1x,p1y),(p1x+dx*2,p1y+dy*2);
    #p1,p2,p3,p4 = p1[0],p1[1],p1[0]+dx*2,p1[1]+dy*2;
    #return p1,p2,p3,p4

#"""
#this might be for future use..
#
#class Item(object):
#    def __init__(self, position,direction,radius):
#        self.px = position[0];
#        self.py = position[1];
#        self.dx = direction[0];
#        self.dy = direction[1];
#        self.v = math.sqrt(self.dx*self.dx+self.dy*self.dy);
#        self.r = radius;
#
#class Obstacle(object):
#    def shipCollision(self, position,direction):
#        return None;
#    def boltCollision(self, position,direction):
#        return None;
#
#class Wall(Obstacle):
#    def __init__(self,begin,end):
#        self.px = begin[0];
#        self.py = begin[1];
#        self.dx = end[0]-begin[0];
#        self.dy = end[1]-begin[1];
#    def shipCollision(self, item):
#        pass;
#    def boltCollison(self, position,direction):
#        pass;
#
#little note for my self:
#import filename
#filename.class
#filename.function
#or:
#from filename import class
#then you can use it normally.
#for function:
#from filename import function
#then just call function by name.
#"""






