class Car:
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()


	def display_all(self):
		print("Price:",self.price)
		print("Speed:",self.speed)
		print("Fuel:",self.fuel)
		print("Mileage:",self.mileage)
		print("Tax:",self.tax)
		print('*' * 80)

mustang = Car(10000,"130mph","Full",15000)
car2= Car(60000,"100mph","Half Full",0)
car3= Car(20000,"110mph","Full",250)
car4= Car(3000,"120mph","Half Full",40)
car5= Car(70000,"130mph","Full",60)
car6= Car(8000,"140mph","Empty",70)
