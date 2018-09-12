class Animal:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return(self)

    def run(self):
        self.health -= 5
        return(self)

    def display_health(self):
        print(self.health)
        return(self)



class Dog(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health = 150
        
    def pet(self):
        self.health += 5
        return(self)


class Dragon(Animal):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return(self)

    def display_health(self):
        super().display_health()
        print('i am dragon')
        return(self)

a = Animal('lucas', 100)
a.walk().walk().walk().run().run().display_health()
print (a.name)
d = Dog('chloe', 50 )
d.walk().walk().walk().walk().run().run().pet().display_health()
print (d.name)
dr = Dragon('python', 200)
dr.fly().fly().display_health()








        





        



