import random
def randInt(max=0, min=0):
    if max == 0 and min == 0:
        print(int(random.random()*100))
    else:
        print(int(random.random()*(max-min)+min))
randInt(max=500,min=50)
