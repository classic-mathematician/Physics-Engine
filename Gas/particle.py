import math


class Particle(object):


	def __init__(self, radius, position, velocity):
		self.radius = radius
		self.position = position
		self.velocity = velocity
		self.mass = 1
		self.history = []



	def round(self):
		self.position[0] = round(self.position[0], 3)
		self.position[1] = round(self.position[1], 3)
		self.velocity[0] = round(self.velocity[0], 3)
		self.velocity[1] = round(self.velocity[1], 3)
