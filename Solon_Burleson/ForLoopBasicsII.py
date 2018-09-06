# Biggie Size

def makeitBig(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list

print(makeitBig([-1,3,5,-5]))

# Count Positives

def countPositives(list):
    count = 0
    for x in range(len(list)):
        if list[x] > 0:
            count += 1
    list[len(list)-1] = count
    return list

print(countPositives([-1,1,1,1]))

# Sum Total

def sumTotal(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum

print(sumTotal([1,2,3,4]))

# Average

def average(list):
    sum = 0
    avg = 0
    for x in range(len(list)):
        sum += list[x]
    avg = sum / len(list)
    return avg

print(average([1,2,3,4]))

# Length

def length(list):
    length = 0
    for x in range(len(list)):
        length+=1
    return length

print(length([1,2,3,4]))

# Minimum

def minimum(list):
    min = list[0]
    if len(list) < 1:
        return false
    else:
        for x in range(len(list)):
            if list[x] < min:
                min = list[x]
    return min

print(minimum([1,2,3,4]))
print(minimum([-1,-2,-3]))

# Maximum

def maximum(list):
    max = list[0]
    if len(list) < 1:
        return false
    else:
        for x in range(len(list)):
            if list[x] > max:
                max = list[x]
    return max

print(maximum([1,2,3,4]))
print(maximum([-1,-2,-3]))

# UltimateAnalyze

def ultimateAnalyze(list):
    min = list[0]
    max = list[0]
    sum = 0
    avg = 0
    for x in range(len(list)):
        if list[x] < min:
            min = list[x]
            sum += list[x]
        elif list[x] > max:
            max = list[x]
            sum += list[x]
        else:
            sum += list[x]
    avg = sum / len(list)
    d = dict()
    d['min'] = min
    d['max'] = max
    d['sum'] = sum
    d['avg'] = avg
    return d

print(ultimateAnalyze([1,2,3,4]))

# ReverseList

def reverseList(list):
    for x in range(int(len(list)/2)):
        temp = list[x]
        list[x] = list[len(list)-1-x]
        list[len(list)-1-x] = temp
    return list

print(reverseList([1,2,3,4]))
