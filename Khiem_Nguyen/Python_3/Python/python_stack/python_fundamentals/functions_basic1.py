#1
def a():
    return 5
print(a())
# expected was 5 and correct

#2
def a():
    return 5
print(a()+a())
# expected was 10 and correct

#3
def a():
    return 5
    return 10
print(a())
# expected was 10 but actual was 5

#4
def a():
    return 5
    print(10)
print(a())
# expected was 5 actual was non

#5
def a():
    print(5)
x = a()
print(x)
# expected was none and correct

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#expected was 8 actual was error?

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#expected was 25 and correct

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#expected 10 and was actuall 100 and 10, i forgot the print

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#expected was 7,14,21 and correct

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#expected was 8 and correct

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#expected was 500,500,300,500 and correct

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#expected 500,500,300,500 and correct

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#expected 500,500,300,300 and correct

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#expected 1,3,2 and correct

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#expected was 1,3,5,10 and correct
