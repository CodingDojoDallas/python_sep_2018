#1
def makeItBig(arr):
    for i in range(0,len(arr)):
        if (arr[i]>0):
            arr[i]="big"
    print(arr)
    return(arr)
makeItBig([-1,2,5,-5])

#2
def countPositives(arr):
    count = 0
    for i in range(0,len(arr)):
        if arr[i]>0:
            count = count + 1
    arr[len(arr)-1] = count
    print(arr)
countPositives([-1,1,1,1])

#3
def sumTotal(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
    print(sum)
sumTotal([1,2,3,4])

#4
def average(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
    average = sum/len(arr)
    print(sum)
    print(len(arr))
    print(average)
average([1,2,3,4])

#5
def length(arr):
    print(len(arr))
length([1,2,3,4])

#6
def minimum(arr):
    if len(arr) == 0:
        return False
    currentMin = arr[0]
    for i in range(0,len(arr)):
        if arr[i] < currentMin:
            currentMin = arr[i]
    print(currentMin);
minimum([1,2,3,4])
minimum([-1,-2,-3])

#7
def maximum(arr):
    if len(arr) == 0:
        return False
    currentMax = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > currentMax:
            currentMax = arr[i]
    print(currentMax)
print(maximum([]))
maximum([1,2,3,4])
maximum([-1,-2,-3])

# #8 original but updated below with feedback
# def analyze(arr):
#     myDict = {"sumTotal":"", "average":"", "minimum":"", "maximum":"", "length":""}
#     sum = 0
#     for i in range(0,len(arr)):
#         sum = sum + arr[i]
#         myDict["sumTotal"] = sum
#         average = sum/len(arr)
#         myDict["average"] = average
#         currentMin = arr[0]
#         for i in range(0,len(arr)):
#             if arr[i] < currentMin:
#                 currentMin = arr[i]
#         myDict["minimum"] = currentMin
#         currentMax = arr[0]
#         for i in range(0,len(arr)):
#             if arr[i] > currentMax:
#                 currentMax = arr[i]
#         myDict["maximum"] = currentMax
#         myDict["length"] = len(arr)
#     print(myDict)
# analyze([1,2,3,4])
#
#8 correction
def analyze(arr):
    myDict = {"sumTotal":"", "average":"", "minimum":"", "maximum":"", "length":""}
    sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
        myDict["sumTotal"] = sum
        average = sum/len(arr)
        myDict["average"] = average
        currentMin = arr[0]
        if arr[i] < currentMin:
            currentMin = arr[i]
            myDict["minimum"] = currentMin
        currentMax = arr[0]
        if arr[i] > currentMax:
            currentMax = arr[i]
            myDict["maximum"] = currentMax
    myDict["length"] = len(arr)
    print(myDict)
analyze([1,2,3,4])
#
# #9 original but updated below with feedback
# def reverse(arr):
#     if len(arr) % 2 == 0:
#         half = int(len(arr)/2) + 1
#     else:
#         half = int(len(arr)/2) + .5
#     for i in range(0,half):
#         temp = arr[i]
#         arr[i] = arr[len(arr)-1-i]
#         arr[len(arr)-1-i] = temp
#     print(arr)
# reverse([1,2,3,4])

9 correction
def reverse(arr):
    if len(arr) % 2 == 0:
        half = int(len(arr)/2) + 1
    else:
        half = int(len(arr)/2) #removed the +.5
    for i in range(0,half):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    print(arr)
reverse([1,2,3,4])
