class bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print(self.price)
        print(self.speed)
        print(self.miles)

    def riding(self):
        self.miles += 10

    def reverse(self):
        self.miles -= 5

bike1 = bike(200, "25mph")
