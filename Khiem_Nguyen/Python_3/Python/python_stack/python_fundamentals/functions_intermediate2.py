#1 data
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1a
z[0]["x"] = 15
print(z)

z[0]["x"] = x[0]
print(z)

z[0]["x"] = x[1]
print(z)

#1b
students[0]["last_name"]= "Bryant"
print(students)

#1c
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#1d
z[0]["y"] = 3

#2 data
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#2
def iterateDictionary(arr):
    for i in range(0,len(arr)):
        print(arr[i])
iterateDictionary(students)

3 data
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#3
def iterateDictionary2(key,arr):
    for i in range(0,len(arr)):
        print(arr[i][key])
iterateDictionary2("first_name",students)



#4 data
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# def printDojoInfo(dict):
#     print(len(dict["locations"]))
# printDojoInfo(dojo)

def printDojoInfo(dict):
    for key in dict:
        print(len(dict[key]))
        print(key.upper())
        print(dict[key])
printDojoInfo(dojo)
