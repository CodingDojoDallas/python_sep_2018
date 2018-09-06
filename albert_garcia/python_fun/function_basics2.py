#1
def countdown(x):
    list = []
    i = x
    while i >= 0:
        list.append(i)
        i -= 1
    print(list)
countdown(5)

#2
def printReturn(x,y):
    print(x)
    return y
b = printReturn(2,3)
print(b)

#3
def firstPlus(x):
    sum = x[0] + len(x)
    print(sum)
firstPlus([2,1,1,1,1])

#4
def greaterSecond(x):
    counter = 0
    lst = []
    if len(x) < 2:
        print(false)
    else:
        for i in x:
            if i > x[1]:
                lst.append(i)
                counter += 1
    print(counter)
    return lst
b = greaterSecond([2,0,1,2,3,0])
print(b)

#5
def lengthAndValue(x,y):
    lst = []
    for i in range(x):
        lst.append(y)
    print(lst)
lengthAndValue(4,7)