from Enemy import Enemy
from items import Weapon, HealingPotion, ManaPotion, StaminaPotion
import random

healing_potion = HealingPotion("Health potion", 30)
stamina_potion = HealingPotion("Stamina potion", 15)
mana_potion = HealingPotion("Mana potion", 20)

sword = Weapon("Flaming sword", 11, "slash")
cleaver = Weapon("BattleAxe", 13, "bash")
bow = Weapon("Ebony Bow", 14, "range")
staff = Weapon("Staff of Magus", 17, "staff")

potion = random.choice([healing_potion, stamina_potion, mana_potion])

enemy = Enemy("Slime", 10)