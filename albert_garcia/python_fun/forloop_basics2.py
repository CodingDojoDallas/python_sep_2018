#1
def makeBig(x):
    count = 0
    for i in x:
        if i > 0:
            x[count] = 'big'
        count += 1
    print(x)
makeBig([-1,2,3,-5])

#2
def countPositives(x):
    count = 0
    for i in x:
        if i > 0:
            count += 1
    print(count)
    x[-1] = count
    print(x)
countPositives([1,2,-3,-2,1])

#3
def sumTotal(x):
    sum = 0
    for i in x:
        sum += i
    print(sum)
sumTotal([1,2,3,4])

#4
def average(x):
    sum = 0
    for i in x:
        sum += i
    print(sum/len(x))
average([1,2,3,4])

#5
def length(x):
    count = 0
    for i in x:
        count += 1
    print(count)
length([1,2,3,4])

#6
def min(x):
    if len(x) > 0:
        temp = 0
        for i in x:
            if i < temp:
                temp = i
        print(temp)
    else:
        return False
min([1,2,3,4])

#7
def max(x):
    if len(x) > 0:
        temp = x[0]
        for i in x:
            if i > temp:
                temp = i
        print(temp)
    else:
        return False
b = max([1,2,3,4])
print(b)

#8
def ultAnalize(x):
    dictionary = {
        "sumTotal": 0,
        "min": x[0],
        "max": x[0],
        "length": len(x)
    }
    for i in x:
        dictionary["sumTotal"] += i
        if i < dictionary["min"]:
            dictionary["min"] = i
        if i > dictionary["max"]:
            dictionary["max"] = i
    print(dictionary)
ultAnalize([1,2,3,4])

#9
def reverse(x):
    for i in range(int(len(x)/2)):
        temp = x[i]
        x[i] = x[(i + 1) * -1]
        x[(i + 1) * -1] = temp
    print(x)
reverse([1,2,3,4])