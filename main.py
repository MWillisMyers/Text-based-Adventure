from Config import *
from Hero import *
from classList import *
import random, os, glob, time


game_state = 0
save_list = []
turn_choice = (1, 2)

experience = 0

location = 0

adjustment = random.randint(1, 3)

while game_state != 5:
	while game_state == 0:
		text = raw_input("Welcome. Type start to begin, for help, type help. ").lower()
		if text == "start":
			game_state = 1
		if text == "help":
			game_state = 9

	while game_state == 1:
		text = raw_input("Would you like to load a save file or Create a new character? ").lower()
		if  text == "load":
			game_state = 8
		if text == "new":
			print "You awake in a dark room. Your eyes may take a moment to adjust."
			time.sleep(adjustment)
			game_state = 2
		if text == "delete":
			delete = raw_input("what file would you like to delete?").lower()
			path = os.path.join("Saves")
			os.remove(os.path.join(path, (str(delete) + '.txt')))

	while game_state == 2:
		name = raw_input("Who Are you?").lower()
		game_state = 3

	warrior = Warrior(name, 45, 45, sword)
	TH = TWarrior(name, 50, 30, cleaver)
	nightengale = Nightingale(name, 35, 20, bow)
	mage = Mage(name, 30, 30, "fireball", staff)

	while game_state == 3:
		player = raw_input("What is your class?").lower()
		if player == "warrior":
			player = warrior
		if player == "berserker":
			player = TH
		if player == "rogue":
			player = nightengale
		#if player == "mage":
			#player = mage
		else: 
			player = random.choice([warrior, TH, nightengale])
		path = os.path.join("Saves")
		fp = open(os.path.join(path, (str(name) + '.txt')), 'w')
		fp.write(str(name) + ", " + str(player) + ", " + str(experience) + ", " + str(location))
		fp.close()
		print ("You are sitting on the cold dungeon floor. The lump on your head suggests you've been unconcious for some time.  ")
		game_state = 4

	def fight(hero, enemy):
		while hero.is_not_RIP() and enemy.is_not_RIP():
			if hero.energy_points >= 10:
				hero.specialAttack(enemy)
				print("%s has %s mana left" % (hero.name, hero.energy_points))
			else:
				hero.attack(enemy)
			if enemy.is_not_RIP():
				enemy.attack(hero)
		if hero.is_RIP():
			print("%s killed %s" % (enemy.name, hero.name))
		else:
			print("%s killed %s. %s has %s hp left" % (hero.name, enemy.name, hero.name, hero.hit_points))

	def drop(player, enemy):
		if enemy.is_RIP:
			item_drop = random.choice(range(1,10))
			if item_drop in [4, 6, 8]:
				player.potion_count += 1
				print ("The %s dropped a %s" % (enemy.name, potion.name))

	while game_state == 4:
		text = raw_input("What will you do?").lower()
		if text == "look": 
			print location
		if text == "save":
			path = os.path.join("Saves")
			fp = open(os.path.join(path, (str(name) + '.txt')), 'w')
			fp.write(str(name) + ", " + str(player) + ", " + str(experience) + ", " + str(location))
			fp.close()
		if text == "fight":
			game_state = 10
		if text == "qq":
			game_state = 5
		if player.is_RIP():
			game_state = 6
		#else:
			#print"I'm afraid you can't do that. Try again"

	while game_state == 6:
		text = raw_input("You've met with a terrible fate, haven't you? Play Again?").lower()
		if text == "yes":
			print"The Oracles of Glenmoril smile upon your soul!"
			game_state = 0
		if text == "no":
			print"Good Bye!"
			game_state = 5

	while game_state == 8:
		print glob.glob("/RPG/Saves/*.txt")
		load = raw_input("What file would you like? ").lower()
		if load == "":
			pass

		if load == "return":
			game_state = 1

	while game_state == 9:
		help = raw_input("Welcome to the help portal.")
		if help == "return":
			game_state = 0

	while game_state == 10:
		print "A Fight has Started!"
		turn = random.choice(turn_choice)
		print "You're fighting %s" % enemy.name
		if turn == 1:
			print "The enemy moves first"
			game_state = 11
		if turn == 2:
			print "It is your turn"
			game_state = 12

	while game_state == 11:
		"""Enemy Turn"""
		if enemy.is_not_RIP():
			enemy.attack(player)
			game_state = 12
		if enemy.is_RIP():
			print "You have won!"
			drop(player, enemy)
			experience += 10
			print "%s has gained 10 experience!" % player.name
			game_state = 4

	while game_state == 12:
		"""Player Turn"""
		if player.is_not_RIP:
			text = raw_input("It is your turn, What will you do? ").lower()
			if text == "attack":
				player.attack(enemy)
				game_state = 11
			if text == "block":
				pass
			if text == "use":
				item = raw_input("What would you like to use?").lower()
				if item == "health potion" and item in inventory:
					player.drink(healing_potion)
					print "%s has %s hp left" % ( player.name, player.hit_points)

				if item == "energy potion" and item in inventory:
					player.drink(energy_potion)
					print "%s has %s energy left" % ( player.name, player.hit_points)
			if text == "flee":
				chance = random.choice(turn_choice)
				if chance == 1:
					print "You are not strong like bull!"
					game_state = 4
				if chance == 2:
					print "You are Paralyzed by fear!"
					game_state = 11
		elif player.is_RIP:
			print "You died!"
			game_state = 6
