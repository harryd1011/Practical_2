tuple = ('Harsh', 12, 7.01, True)
print(tuple)

# b. Write a Python program to create a tuple with numbers and print one item.
tuple = 1,2,3,4,5,6,7
from random import randint
print(tuple[randint(0, len(tuple)-1)])

# c. Write a Python program to add an item in a tuple.
tuple = 5,4,3,2
# add new item '1'
tuple = tuple + (1,)
print(tuple)

# d. Write a Python program to convert a tuple to a string.
# str.join() method
def convertTuple(tup):
    str = ''.join(tup)
    return str
tuple = ('H', 'a', 'r', 's', 'h')
str = convertTuple(tuple)
print(str)

# e. Write a Python program to find the length of a tuple.
tuple = ('H', 'a', 'r', 's', 'h')
print(len(tuple))
