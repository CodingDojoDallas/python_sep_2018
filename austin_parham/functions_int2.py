# x = [ [5,2,3], [10,8,9] ] 
# print(x[1][0])

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andre'
# print(sports_directory)

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = 'Bryant'
# print(students)

# z = [ {'x': 10, 'y': 20} ]
# z[0]['y'] = 30
# print(z)

# students =[
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for i in students:
# 	print((i.items()))

def iterateDict(x,y):
	for i in range(0,len(x)):
		print(x[i][y])
iterateDict([
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
],'first_name')

# def sayThat(x):
# 	print(len(x['locations']), 'LOCATIONS')
# 	for i in range(0,len(x['locations'])):
# 		print(x['locations'][i])
# 	print(len(x['instructors']), 'INSTRUCTORS')
# 	for i in range(0,len(x['instructors'])):
# 		print(x['instructors'][i])
# sayThat({
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# })

	