class Item(object):
	def __init__(self, name):
		self.name = name

class Weapon(Item):
	def __init__(self, name, damage, weapon_type):

		super(Weapon, self).__init__(name)

		self.damage = damage 
		self.weapon_type = weapon_type	

class Spell(Item):
	def __init__(self, name, damage):

		super(Spell, self).__init__(name)
		
		self.damage = damage 
			

class HealingPotion(Item):
	def __init__(self, name, amount):
		super(HealingPotion, self).__init__(name)
		self.amount = amount
	def use(self, target):
		target.set_hit_points(target.hit_points + self.amount)
	def description(self):
		return "heals for %s " % self.amount

class ManaPotion(Item):
	def __init__(self, name, amount):
		super(ManaPotion, self).__init__(name)
		self.amount = amount
	def use(self, target):
		target.set_mana_points(target.mana_points + self.amount)
	def description(self):
		return "restores for %s mana " % self.amount

class StaminaPotion(Item):
	def __init__(self, name, amount):
		super(StaminaPotion, self).__init__(name)
		self.amount = amount
	def use(self, target):
		target.set_stamina_points(target.stamina_points + self.amount)
	def description(self):
		return "restores for %s stamina" % self.amount