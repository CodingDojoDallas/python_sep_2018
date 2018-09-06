# Basic

for x in range(151):
    print(x)

# Multiples of Five

for x in range(5,1000001):
    if x % 5 == 0:
        print(x)

# Counting the Dojo Way

for x in range(1,101):
    print(x)
    if x % 5 == 0:
        print("Coding")
        if x % 10 == 0:
            print("Dojo")
    
# Whoa That Suckers Huge

sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)

# Countdown by Four

for x in range(2018,0,-4):
    print(x)

# Flexible Countdown

lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)
