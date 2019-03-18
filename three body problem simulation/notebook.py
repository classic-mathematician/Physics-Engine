import pygame
import math
from body import Body




pygame.init()

#screen
screen_width = 800
screen_height = 600


#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

colors = []
colors.append(black)
colors.append(white)
colors.append(red)
colors.append(blue)
colors.append(green)



#initialization
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("space")
clock = pygame.time.Clock()

crashed = False


b1 = Body(10, [0,0], [2, 0], green) 
b2 = Body(10, [0, 20], [-1, 0], red)
b3 = Body(10, [-20, -30], [0, 0], blue)


bodies = []
bodies.append(b1)
bodies.append(b2)
bodies.append(b3)

while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True



	screen.fill(black)




	for i in range(len(bodies)):
		pygame.draw.circle(screen, bodies[i].color, bodies[i].encrypt(), 4, 0 )



	for i in range(len(bodies)):
		for k in range(len(bodies)):
			if k != i:
				bodies[i].apply_force(bodies[i].attract(bodies[k]))

	for i in range(len(bodies)):
		bodies[i].apply_velocity()


	pygame.display.update()
	clock.tick(60)


pygame.quit()
quit()

	