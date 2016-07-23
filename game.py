import random

class Enemy():
	life = random.randint(8, 12)

	def attack(self, damage):
		chance = random.randint(1, 100)
		if chance >= 10:
			self.life -= damage
			print ("You hit enemy for " + str(damage) + " damage. Now it has " + str(self.life) + " life.")
			if (self.life <= 0):
				self.die()
		else:
			print ("You missed!")

	def die(self):
		print ("You killed it :))))))")

	def __init__(self):
		print ("\nAn enemy with " + str(self.life) + " life approaches.")


enemy1 = Enemy()

while (enemy1.life > 0):
	choice = input("What do you want to do?\n")
	if 	choice == "attack":
		damage = random.randint(1, 4)
		enemy1.attack(damage)
