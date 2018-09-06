class mathDojo:
    def __init__(self,name):
        self.name = name
        self.value = 0
    def add(self, *perams):
        for i in perams:
            self.value += i
        return self
    def subtract(self, *perams):
        for i in perams:
            self.value -= i
        return self
    def result(self):
        print(self.name, self.value)
        return self.value
md = mathDojo("md")

x = md.add(2).add(2,5,1).subtract(3,2).result()
print(x)