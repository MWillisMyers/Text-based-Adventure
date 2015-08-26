from Class import Entity 
import random 


class Enemy(Entity):
	def attack(self, target):
		damage = random.choice(range(20))
		print "%s attacks %s for %s damage" % (self.name, target.name, damage)
		target.set_hit_points(target.hit_points - damage)

class Boss(Enemy):
	pass

class SpecialEnemy(Enemy):
	pass

class BaseEnemy(Enemy):
	pass

#class EnemyFactory(object):
	#def __init__(self):
	#	enemy = { 
	#		Enemy("Slime", 10000)
	#		Enemy("Goblin", 15000)
	#		Boss("Green Dragon", 13)
		#}
