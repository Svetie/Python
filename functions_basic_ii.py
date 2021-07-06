# 1 Countdown

def countdown(num):
    list = []
    for i in range(-1, num):
        list.append(num)
        num -= 1
    return list

newlist = countdown(5)
print(newlist)

# 2 Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
list_num = [1,2]
sub_two = print_and_return(list_num)
print(sub_two)

# 3 First plus length
def first_plus_length(list):
    length = len(list)
    return list[0] + length

first = first_plus_length(list_num)
print(first)

# 4 Values greater than second
def greater_than_second(list):
    counter = 0
    newList = []
    for i in range(0, len(list)):
        if(len(list) < 2):
            return False
        elif(list[i] > list[1]):
            newList.append(list[i])
            counter += 1
    print(counter)
    return newList
random_list = [5,2,3,2,1,4]
list_than_two = greater_than_second(random_list)
print(list_than_two)

# 5 This length, that value
def length_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
this_length = length_and_value(4, 7)
print(this_length)
print(length_and_value(6, 2))

