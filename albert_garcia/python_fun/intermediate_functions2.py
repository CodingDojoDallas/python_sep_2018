#1
#a)
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

#b)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'bryant'
print(students)

#c)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#d)
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#2
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iteratedict():
    for i in range(len(students)):
        s = ""
        for x, y in students[i].items():
            s += x + " " + "-" + " " + y + " "
        print(s)
        # print(i["first_name"], "last_name -", i["last_name"])
iteratedict()

#3
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iteratedict2(x,y):
    for i in range(len(y)):
        print(y[i][x])
iteratedict2('first_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo():
    temp = ['locations', 'instructors']
    for x in temp:
        print(len(dojo[x]), x)
        for i in dojo[x]:
            print(i)
printDojoInfo()

# alt...
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo(x):
    for key in x.key:
        print(str(len(x.keys()[key])), str(x.keys()[key])
        for i in x[key]:
            print(i)
printDojoInfo(dojo)