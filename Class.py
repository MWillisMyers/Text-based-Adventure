import random
from items import HealingPotion, ManaPotion, StaminaPotion

class Entity(object):

	def __init__(self, name, hit_points):
		self.name = name 
		self.hit_points = hit_points
		self.maximum_hit_points = hit_points
	def set_hit_points(self, hit_points):
		if hit_points < 0:
			self.hit_points = 0
		elif hit_points > self.maximum_hit_points:
			self.hit_points = self.maximum_hit_points
		else: 
			self.hit_points = hit_points

	def attack(self, target):
		raise Exception('You must override')

	def is_RIP(self):
		return self.hit_points == 0

	def is_not_RIP(self):
		return not self.is_RIP()

