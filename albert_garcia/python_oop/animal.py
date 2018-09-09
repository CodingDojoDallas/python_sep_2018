class animal:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display(self):
        print(self.name, "health:", self.health)
        return self

class dog(animal):
    def __init__(self):
        super().__init__(self)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class dragon(animal):
    def __init__(self):
        super().__init__(animal)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display(self):
        super().display()
        print(self.health, "I am a dragon")
        return self

animal1 = animal("cat")
animal1.run().run().walk().display()

animal2 = dog()
animal2.walk().walk().walk().run().run().pet().display()

animal3 = dragon()
animal3.run().run().fly().display()