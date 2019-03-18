import math
import numpy as np


def normalize(v):
	norm = np.linalg.norm(v)
	if norm == 0:
		return v
	return v / norm




class Body(object):


	def __init__(self, mass, position, velocity, color):
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.color = color



	def attract(self, body_2):

		force = list(np.array(body_2.position) - np.array(self.position))
		dist = math.hypot(body_2.position[0] - self.position[0], body_2.position[1] - self.position[1])
		if(dist < 3):
			dist = 3
		#normalization
		force = normalize(force)

		force_magn = self.mass * body_2.mass / (dist**2)

		for i in range(len(force)):
			force[i] *= force_magn

		return force


	def apply_force(self, force):
		self.velocity[0] += force[0]
		self.velocity[1] += force[1]


	def apply_velocity(self):
		self.position[0] += self.velocity[0]
		self.position[1] += self.velocity[1]


	def encrypt(self):
		return [int(self.position[0] + 300), int(300 - self.position[1])]





