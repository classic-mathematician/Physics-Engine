import pygame
import math
from pendulum import Pendulum


pygame.init()

#screen
screen_width = 800
screen_height = 600

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0,255,0)

#initialization
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("space")
clock = pygame.time.Clock()


crashed = False


#pendulum
p1 = Pendulum([0,0], 250, math.pi-0.1, 20)
p2 = Pendulum(p1.bob, 200, math.pi, 30)


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True



    screen.fill(white)
    
    p1_origin, p1_bob = p1.encrypt(400, 200)
    p2_origin, p2_bob = p2.encrypt(p1_bob[0], p1_bob[1])

    # draw first pendulum
    pygame.draw.circle(screen, red, p1_origin, 4, 0)
    pygame.draw.line(screen, black, p1_origin, p1_bob, 1)
    pygame.draw.circle(screen, red, p1_bob, p1.mass, 0)

    # draw second pendulum
    pygame.draw.circle(screen, green, p1_bob, 4, 0)
    pygame.draw.line(screen, black, p1_bob, p2_bob, 1)
    pygame.draw.circle(screen, green, p2_bob, p2.mass, 0)

    p1.accelerate_first(p2)
    p2.accelerate_second(p1)
    p1.update()
    p2.update()

    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()
