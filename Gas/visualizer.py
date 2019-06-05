import pygame
import csv  

time = 100
population = 100


simulation = []

# function that reads the csv asociated with the position of the particles to be later drawn by the visualizer

with open('simulation.csv') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter = ',')) 


    particle_pos = []


    for instant in range(time):

        values = csv_reader[instant]


        simulation_row = []
        for i in range(0,population * 2, 2):
            particle_pos.append(int(float(values[i])))
            particle_pos.append(int(float(values[i+1])))
            particle_pos = []

            simulation_row.append(particle_pos)

        simulation.append(simulation_row)
    


# visualizer settings


# screen
screen_width = 800
screen_height = 800

# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0,255,0)

colors = []

colors.append(black)
colors.append(white)
colors.append(red)
colors.append(blue)
colors.append(green)


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fluid")
clock = pygame.time.Clock()

crashed = False




while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True



    for i in range(time - 1):

        screen.fill(white)
       
        for j in range(population):

            pygame.draw.circle(screen, green, [int(simulation[i][j][0]), int(800 - int(simulation[i][j][1]))], 1, 0)
        
        pygame.display.update()
        clock.tick(60)



    break


    



pygame.quit()
quit()
