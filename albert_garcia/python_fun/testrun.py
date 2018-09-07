class car:
    def __init__(self, name, price, speed,fuel, mileage):
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print(self.name)
        print("price", self.price)
        print("speed:", self.speed)
        print("fuel:", self.fuel)
        print("milage:", self.mileage)
        print("tax:", self.tax)


car1 = car("car1",10000,"80mph", 'full', 5000)
car2 = car("car2", 12000, "100mph", 'not full', 2000)
car3 = car("car3", 20000, "120mph", 'full', 0)
car4 = car("car4", 2000, "60mph", 'not full', 100000)
car5 = car("car5", 7500, "70mph", 'full', 20000)
car6 = car("car6", 9999, "75mph", 'not full', 4500)


car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
