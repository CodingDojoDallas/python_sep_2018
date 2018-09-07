class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles = self.miles+10
        print("Riding")
        return self
    def reverse(self):
        if (self.miles > 0):
            self.miles = self.miles-10
        print("Reversing")
        return self

bike1 = Bike("10", "20")
bike1.ride().ride().ride().reverse().displayinfo()
