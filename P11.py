import sys
import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 400
width = 200
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

kite = [(0, -120), (50, 50), (-0, 120), (-50, 50)]
body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
shape = pymunk.Poly(body, kite)
body.position = 100,200
space.add(body, shape)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
    space.debug_draw(draw_options)
    
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)