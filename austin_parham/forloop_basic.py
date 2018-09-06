for i in range(0,151):
	print(i)

for i in range(5,1000001):
	if i % 5 == 0:
		print(i)

for i in range(1,101):
	if i % 5 == 0:
		print("Coding")
		if i % 10 == 0:
			print("Dojo")
	else:
		print(i)

sum = 0
for i in range(0,500001):
	if i % 2 != 0:
		sum += i
print(sum)

# where is the 'print supposed to be in the indentation'

count = 2018
	print(count)
	count = count - 4

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
	if i % mult == 0:
		print(i)