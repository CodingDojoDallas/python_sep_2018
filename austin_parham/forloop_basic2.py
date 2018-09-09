def biggie(x):
	for i in x:
		if x[i] > 0:
			x[i] = "big"
return x

def posCount(x):
	count = 0
	for i in x:
		if x[i] > 0:
			count = count + 1
	x[len(x) -1] = count
	return x

def arrSum(x):
	sum = 0
	for i in x:
		sum = sum + x[i]
	return sum

def arrAvg(x):
	sum = 0
	for i in x:
		sum = sum + x[i]
	return sum / len(x)

def length(x):
	return len(x)

def minArr(x):
		if len(x) >= 1:
	...     min = x[0]
	...     for i in range(0,len(x)):
	...             if x[i] < min:
	...                     min = x[i]
	...     return min
		else:
			return "False"

def maxArr(x):
...     if len(x) >= 1:
...             max = x[0]
...             for i in range(0,len(x)):
...                     if x[i] > max:
...                             max = x[i]
...             return max
...     else: return "False"

def ultAnalyze (x):
	sum = 0
	min = x[0]
	max = x[0]
	for i in range(0,len(x)):
		if x[i] > max:
			max = x[i]
		if x[i] < min:
			min = x[i]
		sum = sum + x[i]

	dict = {
	"sumTotal" : sum,
	"avg": sum / len(x),
	"minimum" : min,
	"maximum" : max,
	"arrayLength" : len(x)
	}
	print(dict)
	return dict
ultAnalyze([3,2,4,1])


def reverse(x):
	half = 0
	if len(x) % 2 == 0:
		half = int((len(x)/2) + 1)
	else:
		half = int((len(x)/2) + 0.5)
	for i in range(0,half):
		temp = x[i]
		x[i] = x[len(x) - 1 - i]
		x[len(x) -1 - i] = temp
	print(x)
	return x
reverse([1,2,3,4,5])