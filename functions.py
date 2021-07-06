# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful() # output: good morning (repeated on 2 lines)
be_cheerful("tim") # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john") # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6) # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5) # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb") # output: good morning kb (repeated on 3 lines)

# no arguments are provided -- the defaults are used
# one unnamed argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used
# one named argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
# both unnamed arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)
# both named arguments provided -- values are assigned to associated parameter (and then order doesn't matter!)

def be_cheerful(name=""):
    print(f'Good morning {name}')

be_cheerful('Adrien')

# NOT woring
def multiply(num_list, num):
    for x in num_list:
        x *= num # neet to write num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output: [2,4,10,16]

# working
def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[10,20,50,80]



