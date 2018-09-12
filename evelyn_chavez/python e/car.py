class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price 
        self.speed= speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax =.12
        self.display_all()

    def display_all(self):
        print ("price: "+ str(self.price))
        print ("Speed: "+ str(self.speed) + " mph")
        print ("Fuel: "+ str(self.fuel))
        print ("Mileage: "+ str(self.mileage) + " mph")
        print ("Tax: "+ str(self.tax))
        return(self)

car1 = Car(2000, 35, "full", 15)
car2 = Car(2000, 5, "not full", 105)
car1 = Car(2000, 15, "kind of full", 95)
car2 = Car(2000, 25, "full", 25)
car1 = Car(2000, 45, "empty", 15)
car2 = Car(2000000, 35, "empty", 15)