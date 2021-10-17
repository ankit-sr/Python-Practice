'''
    Set is a collection in a python. A set is mutable, onordered collection of distinct values of any type.
    A set can not contain duplicate values and it does not support indexing.
    The elements are bound inside {}.
'''

# Creating a set
fruits = {'apple', 'banana', 'mango'}

# A set can also be created using a constructor
# fruits = set(('apple', 'banana', 'mango'))

print(type(fruits), fruits)

# add() - adding a single item to a set
fruits.add('Kiwi')

# update() - adding an iterable to a set such as a list, tuple, another set, dictionary, etc.
fruits.update([1, 2, 3])

# remove() - removes an item from a set, it raises an exception (KeyError) if the given item is not found in the set
fruits.remove('banana')

# discard() - removes an item from a set, it does not raise an exception if the given item is not found in the set
fruits.discard('Papaya')

# accessing elements of set can not include indexing, thus we can use 'in' keyword and for loop
for element in fruits:
    print(element)

# returns True or False if the element is present in the set or not respectively.
print('papaya' in fruits)


print(fruits)

