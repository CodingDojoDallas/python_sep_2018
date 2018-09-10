def a():
    return 5
print(a())   # Prediction = 5

def a():
    return 5
print(a()+a()) # Prediction = 10

def a():
    return 5
    return 10
print(a())   # Prediction = 10, Answer = 5 -- once a function sees a return it leaves the function entirely.

def a():
    return 5
    print(10)
print(a()) # Prediction = 5

def a():
    print(5)
x = a()
print(x) # Prediction = Nothing is returned or printed because the function was never called

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # Prediction = 8

def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # Prediction = 2+5 Answer = 25, Strings are just put right next to eachother.

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())  # Prediction = 100, 10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # 7
print(a(5,3)) # 14
print(a(2,3) + a(5,3)) # 7 + 14 = Prediction = 21

def a(b,c):
    return b+c
    return 10
print(a(3,5)) #Prediction = 8

b = 500
print(b) # 500
def a():
    b = 300
    print(b)
print(b) # 500
a() # 300
print(b) # 300 Answer = 500, since a value was never returned to REPLACE b, the value of b is still 500 outside of the function 

b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b
print(b) # 500
a() # 300 output got 300 300
print(b) # 300 

b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 300
    return b
print(b) #500
b=a() # 300
print(b) #300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # Prediction 1,3,2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) # Prediction 1,3,5,10. In CMD, the y = a() automatically output values. What does this mean??