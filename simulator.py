import pygame
import random
import time as t
import numpy as np
import math
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from particle import Particle




history = []


# fluid functions

def check_collition(p1, p2):
    distance = math.sqrt((p2.position[0] - p1.position[0])**2 + (p2.position[1] - p1.position[1])**2)

    if (distance <= (p1.radius + p2.radius)):
        collide(p1,p2)


# function that calculates the position and velocity of 2 particles after an elastic collition
def collide(p1, p2):
    term = np.dot(np.subtract(p1.velocity, p2.velocity), np.subtract(p1.position, p2.position)) / (p1.radius + p2.radius)**2    
    sub = np.subtract(p1.position, p2.position)
    sub[0] *= term
    sub[1] *= term

    p1.velocity = np.subtract(p1.velocity, sub)

    p1.position[0] += round(p1.velocity[0] * 0.35, 3)
    p1.position[1] += round(p1.velocity[1] * 0.35, 3)

    sub[0] *= -1
    sub[1] *= -1

    p2.velocity = np.subtract(p2.velocity, sub)

    p2.position[0] += round(p2.velocity[0] * 0.4, 3)
    p2.position[1] += round(p2.velocity[1] * 0.4, 3)


# function that calls the particle round method on all the population to round their relative positions and velocities to 3 digits of precision
def round_population(population):
    for i in range(len(population)):
        population[i].round()
    


# function that modifies the velocity of a particle by the force excerted by a wall with infinite mass
def check_collide_wall(p1):

    if (p1.position[0] <= 2):
        p1.velocity[0] *= -1


    if (p1.position[0] >= 798):
        p1.velocity[0] *= -1

    if (p1.position[1] <= 2):
        p1.velocity[1] *= -1

    if (p1.position[1] >= 798):
        p1.velocity[1] *= -1


    
# function that generates a particle population with a random velocity and a position given by a grid with side sqrt(n), where n is a perfect square
def generate_population(n):

    particle_population = []


    side = round(750 * math.sqrt(1/n), 3)

    perf_side = math.sqrt(n)

    for i in range(1, n + 1):

        pos_x = ((side*i) - (side/2)) % 800
        pos_y = int(i/perf_side) * side - (side/2)

        pos = [pos_x, pos_y]

        velocity = [round(random.randint(-10, 10), 3), round(random.randint(-10, 10), 3)]

        p = Particle(5, pos, velocity)

        particle_population.append(p)

    return particle_population

# function that adds the velocity to the position vector of the particle
def update_position(p1,step):
    p1.position[0] += p1.velocity[0] * step
    p1.position[1] += p1.velocity[1] * step


# function that stores te population position in history data set
def update_population_position(population, history, time):
    frozen_time = []

    for i in range(len(population)):
        frozen_time.append([population[i].position[0], population[i].position[1]])
        update_position(population[i], 0.1)

    history.append(frozen_time)
      


population = generate_population(100)



# main loop of the simulation, where the argument is the time wanted to
for time in range(100):

    print(time)

    update_population_position(population, history, time)


    for i in range(len(population)):
        check_collide_wall(population[i])


    for i in range(len(population)):

        for j in range(i+1, len(population)):

            check_collition(population[i], population[j])

        round_population(population)


    time += 1


# particles position storage

rows = []

for i in range(time):

    row = []
    for j in range(len(population)):
        row.append(history[i][j][0])
        row.append(history[i][j][1])

    rows.append(row)



with open('simulation.csv', 'w', newline = '') as csvFile:
    writer = csv.writer(csvFile)

    writer.writerows(rows)


csvFile.close()

# cloud setup

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(credentials)

sheet = client.open("gas").sheet1  # Open the spreadhseet


for i in range(time):
    sheet.insert_row(rows[i], i+1)

    if ((i + 1) % 50 == 0):
        
        if(i == time - 1):
            break

        print(i)

        t.sleep(101)





