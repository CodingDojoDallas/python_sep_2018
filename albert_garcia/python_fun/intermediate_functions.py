def becheerful(str='', repeat=1):
    print(f"good {str}"*repeat)
becheerful(str= "morning!",repeat=98)

import random
def randInt(max=100,min=0):
    print(int(random.random() * (max - min)) + min)
randInt(max=500, min=50)