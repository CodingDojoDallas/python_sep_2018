class Animal:
	def __init__(self,name,health):
		self.name = name
		self.health = health
	
	def walk(self,x):
		self.health = self.health - (1 * x)
		return self
	
	def run(self,x):
		self.health = self.health - (5 * x)
		return self
	
	def display_health(self):
		print(self.name)
		print(self.health)
		print('*' * 80)

# zebra = Animal('zebra',100)

# zebra.walk(3).run(2).display_health()

class Dog(Animal):
	def __init__(self,name,health):
		super().__init__(name,150)
		# self.health = 150

	def pet(self):
		self.health = self.health + 5
		return self

dog = Dog('fido',100)

# dog.walk(3).run(2).pet().display_health()

class Dragon(Animal):
	def __init__(self,name,health):
		super().__init__(name,170)

	def fly(self,x):
		self.health = self.health - (10 * x)
		return self

	def display_health(self):
		super().display_health()
		print("I am a Dragon!")

dragon = Dragon('blue',100)

dragon.fly(1).display_health()