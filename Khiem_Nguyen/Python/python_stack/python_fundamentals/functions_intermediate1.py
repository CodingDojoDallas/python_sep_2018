import random
#1
def randInt():
    print(int(random.random()*100))
randInt()

2
def randInt(max=50):
    print(int(random.random()*50))
randInt()

3
def randInt(min=50):
    print(int(random.random()*50+50))
randInt()

#4
def randInt(min=50,max=500):
    print(int(random.random()*450+50))
randInt()
