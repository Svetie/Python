#tuples caanot be changed (immutable)

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

# A tuple can be used to group any number of items into a single compound value. 
# Syntactically, a tuple is a comma-separated sequence of values. 
# Although it is not necessary, it is conventional to enclose tuples in parentheses.

dog = ("Canis Familiaris", "dog", "carnivore", 12)

# we can add and slice tuples
dog = dog + ("domestic",) #result is...("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:] #result is..("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")


# tuple functions
max(sequence) #returns the largest value in the sequence
sum(sequence) #return the sum of all values in sequence
enumerate(sequence) # used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
map(function, sequence) # applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) # returns the lowest value in a sequence.
sorted(sequence) # returns a sorted sequence

# tuple as return value
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
