def countdown(x):
	newarr = []
	for i in range(x,-1,-1):
		newarr.push(i)
	return newarr

def printReturn(x,y):
	print(x)
	return y

def plusLength(x):
	sum = len(x) + x[0]
	print sum

def greaterThan(x):
	count = 0
	newarr = []
	if len(x) > 1:
		for i in x:
			if x[i] > x[1]:
				count = count + 1
				newarr.append(x[i])
	else:
		return "False"
	print(newarr)
	return count


def lengthAndValue(size,value):
	newarr = []
	for i in range(0,size):
		newarr.append(value)
