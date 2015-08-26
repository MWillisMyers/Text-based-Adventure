from Class import Entity 
import random

class BaseCharacter(Entity):
	inventory_size = 9
	weapon_type_blacklist = []
	inventory = []
	potion_count = 0

	def __init__(self, name, hit_points, weapon):
		super(BaseCharacter, self).__init__(name, hit_points)
		self.weapon = weapon	

	def damage_formula(self):
		return random.choice(range(1,11))

	def talk(self):
		print("Ey LMAO")

	def item(self):
		print("You used the ")

	def drink(self, potion):
		potion.use(self)
		print("you use %s it %s" % (potion.name, potion.description()))

	def attack(self, target):
		damage = self.damage_formula()
		if self.weapon.weapon_type in self.weapon_type_blacklist:
			damage = int(damage / 2)
		print "%s attacks %s with the %s for %s damage" % (self.name, target.name, self.weapon.name, damage)
		target.set_hit_points(target.hit_points - damage)

	def move(self):
		pass

	def block(self):
		pass

	def equip(self):
		#is the item in the inventory?
		pass

	def ride(self):
		pass

class Melee(BaseCharacter):
	inventory_size = 12
	def __init__(self, name, hit_points, energy_points, weapon):
		super(Melee, self).__init__(name, energy_points, weapon)
		self.weapon = weapon
		self.energy_points = energy_points
		self.maximum_energy_points = energy_points

	def damage_formula(self):
		return self.weapon.damage + random.choice(range(1,11))

	def special_damage_formula(self):
		return self.weapon.damage + random.choice(range(5,20))

	def set_energy_points(self, energy_points):
		if energy_points < 0:
			self.energy_points = 0
		elif energy_points > self.maximum_energy_points:
			self.energy_points = self.maximum_energy_points
		else: 
			self.energy_points = energy_points

class Magic(BaseCharacter):
	inventory_size = 9
	def __init__(self, name, hit_points, energy_points, spell, weapon):
		super(Magic, self).__init__(name, energy_points, weapon)
		self.spell = spell
		self.weapon = weapon
		self.energy_points = energy_points
		self.maximum_energy_points = energy_points	

	def damage_formula(self):
		return self.weapon.damage + random.choice(range(1,11))

	def special_damage_formula(self):
		return self.weapon.damage + random.choice(range(5,20))

	def set_energy_points(self, energy_points):
		if energy_points < 0:
			self.energy_points = 0
		elif energy_points > self.maximum_energy_points:
			self.energy_points = self.maximum_energy_points
		else: 
			self.energy_points = energy_points

class Stealth(BaseCharacter):
	inventory_size = 6
	def __init__(self, name, hit_points, energy_points, weapon):
		super(Stealth, self).__init__(name, energy_points, weapon)
		self.weapon = weapon
		self.energy_points = energy_points
		self.maximum_energy_points = energy_points

	def damage_formula(self):
		return self.weapon.damage + random.choice(range(1,11))

	def special_damage_formula(self):
		return self.weapon.damage + random.choice(range(5,20))

	def set_energy_points(self, energy_points):
		if energy_points < 0:
			self.energy_points = 0
		elif energy_points > self.maximum_energy_points:
			self.energy_points = self.maximum_energy_points
		else: 
			self.energy_points = energy_points

class Warrior(Melee):
	def ride(self):
		print("You ride a tawny Horse")

	def item(self):
		print("You used the Star of Glenmoril")

	def move(self):
		print("You move with the determination of an army")

	def specialAttack(self, target):
		damage = self.damage_formula()
		if self.weapon.weapon_type in self.weapon_type_blacklist:
			damage = int(damage / 2)
		print "%s uses a special attack against %s with the %s for %s damage. It costs 10 energy" % (self.name, target.name, self.weapon.name, damage)
		target.set_hit_points(target.hit_points - damage)
		self.set_energy_points(self.energy_points - 10)

class TWarrior(Melee):
	def ride(self):
		print("You ride a horse armed to the teeth")

	def item(self):
		print("You paint yourself in the way of the ancients")

	def move(self):
		print("You move as an angel of death across the field")

	def specialAttack(self, target):
		damage = self.damage_formula()
		if self.weapon.weapon_type in self.weapon_type_blacklist:
			damage = int(damage / 2)
		print "%s uses a special attack against %s with the %s for %s damage. It costs 10 energy" % (self.name, target.name, self.weapon.name, damage)
		target.set_hit_points(target.hit_points - damage)
		self.set_energy_points(self.energy_points - 10)

class Mage(Magic):
	def ride(self):
		print("You ride a horse armed to the teeth")

	def item(self):
		print("You paint yourself in the way of the ancients")

	def move(self):
		print("You move as an angel of death across the field")

	def specialAttack(self, target):
		damage = self.special_damage_formula()
		if self.weapon.weapon_type in self.weapon_type_blacklist:
			damage = int(damage / 2)
		print "%s casts %s with the %s for %s damage" % (self.name, self.spell.name, self.weapon.name, damage)
		target.set_hit_points(target.hit_points - damage)
		self.set_energy_points(self.energy_points - 10)

class Nightingale(Stealth):
	def ride(self):
		print("You ride a horse as black as soot")

	def item(self):
		print("You used the ring of Hircine")

	def move(self):
		print("You move as a shadow")

	def specialAttack(self, target):
		damage = self.damage_formula()
		if self.weapon.weapon_type in self.weapon_type_blacklist:
			damage = int(damage / 2)
		print "%s uses a special attack against %s with the %s for %s damage. It costs 10 energy" % (self.name, target.name, self.weapon.name, damage)
		target.set_hit_points(target.hit_points - damage)
		self.set_energy_points(self.energy_points - 10)