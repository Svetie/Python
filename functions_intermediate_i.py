# 1 Update values in dictionaries and lists
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

# change 10 to 15 in x
x[1][0] = 15
print(x)

# change last name of the first student from Jordan to Bryant
print(students[0]['last_name'])
students[0]['last_name'] = 'Bryant'
print(students)
# change Messi to Andres 
print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# change 20 in z to 30
print(z[0]['y'])
z[0]['y'] = 30
print(z)

# 2 Iterate through a list of dictionaries
def iterateDictionary(some_list):
    for i in some_list:
        print('first_name' + ' - ' + i['first_name'] + ', last_name - ' + i['last_name'])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

# 3 Get values from a list of dictionaries
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
iterateDictionary2('last_name', students) 

# 4 Iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# print(dojo['locations'][0])
# print(len(dojo['locations']))
# print(dojo.keys())

def printInfo(dictionary):
    for key in dictionary:
        print(len(dictionary[key]), key.upper())
        for i in dictionary[key]:
            print(i)

printInfo(dojo)

