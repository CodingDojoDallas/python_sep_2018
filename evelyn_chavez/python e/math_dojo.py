class MathDojo:
    def __init__(self):
        self.sum = 0


    def add(self, *arg):
        for i in arg:
            self.sum += i
        return(self)

    def subtract(self, *arg):
        for i in arg:
            self.sum -= i
        return(self)

    def result(self):
        print(self.sum)

x = MathDojo().add(2).add(2,5,1).subtract(3,2).result()
print(x)

