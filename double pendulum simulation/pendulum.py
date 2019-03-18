import math


class Pendulum(object):


	def __init__(self, origin, arm, angle, mass):
		self.origin = origin
		self.arm = 	arm
		self.angle = angle
		self.mass = mass
		self.bob = [self.origin[0] + math.floor(self.arm * math.sin(self.angle)), self.origin[1] - math.floor(self.arm * math.cos(self.angle))]
		self.angular_velocity = 0	
		self.angular_acceleration = 0


	def encrypt(self, x_displacement, y_displacement):
		new_origin = [x_displacement, y_displacement]
		new_bob = [self.bob[0] + x_displacement, y_displacement - self.bob[1]]
		return new_origin, new_bob

	
	def update(self):
		self.angle += self.angular_velocity
		self.angular_velocity += self.angular_acceleration
		self.bob[0] = math.floor(self.arm * math.sin(self.angle))
		self.bob[1] = -math.floor(self.arm * math.cos(self.angle))
		if(self.angular_velocity > 0):
			self.angular_velocity -= 0.0003
		else:
			self.angular_velocity += 0.0003
		

	#double pendulum exclusive functions
	def accelerate_first(self, p2):
		g = 0.75
		numerator = -g * (2*self.mass + p2.mass)*math.sin(self.angle) - (p2.mass * g * math.sin(self.angle - 2 * p2.angle)) - 2 * math.sin(self.angle - p2.angle) * p2.mass * (p2.angular_velocity**2 * p2.arm + self.angular_velocity**2 * p2.arm * math.cos(self.angle - p2.angle))
		denominator = self.arm * (2 * self.mass + p2.mass - p2.mass * math.cos(2* self.angle - 2*p2.angle))
		self.angular_acceleration = numerator/denominator
		
	
	def accelerate_second(self, p1):
		g = 0.75
		numerator = 2 * math.sin(p1.angle - self.angle) * (p1.angular_velocity**2 * p1.arm * (p1.mass + self.mass) + g * (p1.mass + self.mass) * math.cos(p1.angle) + self.angular_velocity**2 * self.arm * self.mass * math.cos(p1.angle - self.angle))
		denominator = self.arm * (2*p1.mass + self.mass - self.mass * math.cos(2 * (p1.angle - self.angle)))
		self.angular_acceleration = numerator/denominator

		


		

