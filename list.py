ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

#  list do not have to be of the same data type. A list can be a mixture of any Python data types
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# access values

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

# add item to list
x = [1,2,3,4,5]
x.append(99)
print(x) #the output would be [1,2,3,4,5,99]

# [ ] characters to return a copy of the list, constrained to the specified indices. This can be thought of as behaving like the slice function in JavaScript. 
# The starting index and ending index should be separated by the ":" character.
x = [99,4,2,5,-3]
print(x[:]) #the output would be [99,4,2,5,-3]
print(x[1:]) #the output would be [4,2,5,-3];
print(x[:4]) #the output would be [99,4,2,5]
print(x[2:4]) #the output would be [2,5];

# list.append(x)
# Add an item to the end of the list; equivalent to a[len(a):] = [x].

# list.extend(L)
# Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.index(x)
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(cmp=None, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list, in place.

list.extend(list2) # adds all values from a second sequence to the end of the original sequence.
list.pop(index) # remove a value at given position. if no parameter is passed, defaults to final value in the list.
list.index(value) #returns the index position in a list for the given parameter.




