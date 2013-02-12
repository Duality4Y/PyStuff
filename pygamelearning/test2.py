import pygame
from pygame.locals import *


def render_ball_simple(radius, color):
    """ Returns (surf,rect) containing a picture of 
         a circle of the radius, and color given.
    """
    size = radius * 2
    surf = pygame.Surface((size, size))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf, surf.get_rect()

def max(x, y):
    """ returns x, unless x > y.  if it is it returns y.
    """
    if x > y:
        return y
    else:
        return x


def render_ball_funky(radius, color):
    """ Returns (surf,rect) containing a picture of 
         a slightly shaded ball of the radius, and color given.
    """

    size = radius * 2
    surf = pygame.Surface((size, size))

    # we progressively draw smaller circles of different colors.
    increment = int(radius / 4)
    for x in range(4):
        iradius = radius - (x * increment)
        print iradius
        isize = iradius * 2
        icolor = [0,0,0]

        # we increment the color.  if it is bigger than 255 we make it 255.
        icolor[0] = max(color[0] + (x * 15), 255)
        icolor[1] = max(color[1] + (x * 15), 255)
        icolor[2] = max(color[2] + (x * 15), 255)

        pygame.draw.circle(surf, icolor, (radius, radius), iradius)

    

    return surf, surf.get_rect()

def render_ball(radius, color):
    """ Returns (surf,rect) containing a picture of 
         a ball of the radius, and color given.
    """
    # we use the kind of funk one...
    return render_ball_funky(radius, color)



def main():


    pygame.init()

    display_flags = DOUBLEBUF
    width, height = 640, 480

    if pygame.display.mode_ok((width, height), display_flags ):
        screen = pygame.display.set_mode((width, height), display_flags)


    run = 1

    clock = pygame.time.Clock()

    # draw some graphics to surfaces.
    ball1,ball1_rect = render_ball_funky(10, (50, 200, 200))
    ball2,ball2_rect = render_ball_simple(6, (50, 200, 200))

    # move the simple one towards the center top of the screen.
    ball2_rect.x = 200


    while run:

        events = pygame.event.get()

        for event in events:
            
            if event.type == QUIT or (event.type == KEYDOWN and 
                                      event.key in [K_ESCAPE, K_q]):
                # set run to 0 makes the game quit.
                run = 0

        # add the game play in here later.
        screen.blit(ball1, ball1_rect)
        screen.blit(ball2, ball2_rect)


        pygame.display.flip()

        # limit the game to about 40fps, or 40 ticks per second.
        clock.tick(40)


# this runs the main function if this script is called to run.
#  If it is imported as a module, we don't run the main function.
if __name__ == "__main__":
    main()
