# 1
for i in range(1,151):
    print(i)

# 2
count = 5
while count <= 5000:
    print(count)
    count += 5

# 3
count = 1
while count <= 100:
    if count % 5 == 0 and count % 10 == 0:
        print('coding dojo')
    elif count % 5 == 0:
        print('coding')
    else:
        print(count)
    count += 1

# 4
sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)

# 5
i = 2018
while i > 0:
    print(i)
    i -= 4

# 6
def flex(low,high,mult):
    for i in range(low,high + 1):
        if i % mult == 0:
            print(i)
flex(2,9,3)

#predict 1
list = [3,5,1,2]
for i in list:
    print(i)
# 3,5,1,2

#predict 2
list = [3,5,1,2]
for i in range(list):
    print(i)
# list is not an integer to use for range

#predict 3
list = [3,5,1,2]
for i in range(len(list)):
    print(i)
# 0,1,2,3