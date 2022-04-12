dict = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40
}
# function to check given key already exists or not
def check(dict, key):
    if key in dict.keys():
        print(dict[key], " Present")
    else:
        print("key is Not Present")
key = 'c'
check(dict, key)
key = 'm'
check(dict, key)

# b. Write a Python script to merge two Python dictionaries.
# dictionaries
dict1 = {
    'a': 1, 
    'b': 2
}
dict2 = {
    'c': 3,
    'd': 4
}
# To merge dict using update() method
def merge(dict1, dict2):
    return(dict2.update(dict1))
# This return None
print(merge(dict1, dict2))
# changes made in dict2
print(dict2)

# c. Write a Python program to sum all the items in a dictionary.
# dictionarie
dict = {
    'a' : 10,
    'b' : 20,
    'c' : 30
}
# function to return sum
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum
print("Sum : ", returnSum(dict))

# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# Sample Dictionary
dict = {
    0 : 10,
    1 : 20
}
print("Sample Dictionary : ", dict)
# add new key
dict[2] = 30
print("Expected Result : ", dict)

# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
result = {}
# function to update new dictionaries
for i in (dic1, dic2, dic3):
    result.update(i)
print(result)
