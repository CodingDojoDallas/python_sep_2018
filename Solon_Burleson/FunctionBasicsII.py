# Countdown
def Countdown(num):
    while num >= 0:
        print(num)
        num -= 1

Countdown(5)

# Print first return second

def PrintReturn(list):
    print(list[0])
    return list[1]

PrintReturn([1,2])

#First Plus Length

def FirstPlusLength(list):
    sum = list[0] + len(list)
    return sum

# Values Greater than Second

def GreaterthanSecond(list):
    newlist = []
    count = 0
    if len(list) <= 1:
        return false
    for x in range(len(list)):
        if list[x] > list[1]:
            newlist.append(list[x])
            count += 1
    print(count)
    return newlist

# Length and Value

def LengthandValue(a,b):
    list = []
    while a > 0:
        list.append(b)
        a -= 1
    return list

print(LengthandValue(4,7))