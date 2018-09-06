class bike:
    def __init__(self,name, price,speed):
        self.name = name
        self.price = price
        self.speed = speed
        self.miles = 0
    def displayinfo(self):
        print(self.name, "price:", self.price, "speed:", self.speed, "total miles:", self.miles)
        return self
    def ride(self):
        self.miles += 10
        print(self.name, "riding: total miles =", self.miles)
        return self
    def reverse(self):
        if self.miles > 5:
            self.miles -= 5
        print(self.name, "Reversing: total miles =", self.miles)
        return self

bike1 = bike("bike1",200,"25mph")
bike2 = bike("bike2", 300, "30mph")
bike3 = bike("bike2", 150, "20mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()

