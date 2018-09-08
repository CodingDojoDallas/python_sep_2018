class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayAll()
    
    def displayAll(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed))
        print("Fuel: " + str(self.fuel))
        print("Mileage: " + str(self.mileage))
        print("Tax: " + str(self.tax))

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(11000, "100mph", "Full", "10mpg")
car3 = Car(10000, "90mph", "Half", "20mpg")
car4 = Car(9000, "80mph", "Empty", "25mpg")

