class Animal:
    def __init__(self):
        self.name = "animal"
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print(self.health)
        return self


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")
        