def randInt():
	import random
	hold = (random.random()*100)
	hold = int(hold)
	print(hold)
randInt()

def randInt():
	import random
	hold = (random.random()*50)
	hold = int(hold)
	print(hold)
randInt()

def randInt():
	import random
	hold = (random.uniform(50,100))
	hold = int(hold)
	print(hold)
randInt()

def randInt(): #alternate method without uniform
	import random
	hold = (random.random()*100)
	hold = int(hold)
	while hold < 50:
		hold = (random.random()*100)
	hold = int(hold)
	print(hold)
randInt()

def randInt():
	import random
	hold = (random.uniform(50,500))
	hold = int(hold)
	print(hold)
randInt()

def randInt(): #alternate method without uniform
	import random
	hold = (random.random()*500)
	hold = int(hold)

	while hold < 400:
		hold = (random.random()*500)
	hold = int(hold)
	print(hold)
randInt()