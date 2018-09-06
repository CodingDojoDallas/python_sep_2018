#1

def countDown(x):
    arr = []
    for count in range(x,0,-1):
        arr.append(count)
    print(arr)
    return arr
countDown(5)


2
def printReturn(x,y):
    print(x)
    return y
printReturn(1,2)

#3
def firstPlusLength(arr):
    print (arr[0]+ len(arr))
firstPlusLength([2,5,10,15])

4


def greaterThan2(arr):
    count = 0
    newArr = []
    if len(arr) == 1:
        return False
    for i in range(0,len(arr)):
        if arr[i]>arr[1]:
            newArr.append(arr[i])
            count = count + 1
    print(newArr)
    print(count)
greaterThan2([1,2,3,4,5,6])
print(greaterThan2([1]))

5
def lengthAndValue(size,value):
    newArr = []
    for count in range(0,size):
        newArr.append(value)
    print(newArr)
    return(newArr)
lengthAndValue(4,7)
