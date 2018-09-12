class Bike:
    def __init__(self, price, max, miles):
        self.price = price 
        self.max = max
        self.miles = 0

    def displayinfo(self):
        print('the bike price is '+str(self.price))
        print('maximun speed is '+str(self.max))
        print('total miles are ' +str(self.miles))
        return(self)

    def ride(self):
        print('Riding') 
        self.miles += 10
        return(self)

    def reverse(self):
        print('revers')
        self.miles -= 5
        return(self)

bike1 = Bike('$300', '60mph', '100miles')
bike1.ride().ride().ride().reverse().displayinfo()
bike2 = Bike('$500', '40mph', '80miles')
bike2.ride().ride().reverse().reverse().displayinfo()
bike3 = Bike('$600', '80mph', '60miles')
bike3.reverse().reverse().reverse().displayinfo()




        
