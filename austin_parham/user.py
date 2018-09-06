class Bike:
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print(self.price)
		print(self.max_speed)
		print(self.miles)
		print('*' * 80)

	def ride(self):
		print("Riding...")
		print("......")
		print("......")
		self.miles = self.miles + 10

	def reverse(self):
		print("Reversing...")
		print("......")
		print("......")
		self.miles = self.miles - 5

	# def reverse(self):
	# 	print("Reversing...")
	# 	print("......")
	# 	print("......")
	# 	self.miles = self.miles + 5
	# Would use to not subtract miles from reversing

bike1 =	Bike(200,120,20000)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(600,150,5000)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

lance = Bike(4000,900,60000)
lance.reverse()
lance.reverse()
lance.reverse()
lance.displayInfo()
