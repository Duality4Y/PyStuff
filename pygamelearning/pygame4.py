import cairo
import pygame

width = 300
height = 200

pygame.init()
pygame.fastevent.init()
clock = pygame.time.Clock()
sdl_surface = pygame.display.set_mode((width, height))

c_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(c_surface)

while True:
    pygame.fastevent.get()
    clock.tick(30)
    ctx.rectangle(10, 10, 50, 50)
    ctx.set_source_rgba(0.0, 0.0, 0.0, 1.0)
    ctx.fill_preserve()

    dest = pygame.surfarray.pixels2d(sdl_surface)
    dest.data[:] = c_surface.get_data()
    pygame.display.flip()
