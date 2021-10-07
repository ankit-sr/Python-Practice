'''
    Dictionary is again a structure in python which comprises of key-value pairs.
    A typically dictionary holds some word(or element) called as key and its meaning 
    called as value.
    A key can be of any immutable data-type such as int, float, string, boolean, but should not be
    repeated within a dictionary,
    while a value can be anything.
'''

person = {
    'name': 'Prateek',
    'age': 21,
    1001: 'Python',
    True: 'buses'
}


# methods of dictionary

# accessing elements from a dictionary
print(person['name'])
print(person.get('age'))    # returns None, if key is not present

# update() - inserts a new key-value pair in the dictionary
person.update({'family': 'Goutam'})

# keys() -  returns all the keys of the dict
print(person.keys())    # output - dict_keys(['name', 'age', 1001, True, 'family'])

# values() - returns 
print(person.values())  # output - dict_values(['Prateek', 21, 'Python', 'buses', 'Goutam'])

# items() - returns key-value as a pairs
print(person.items())   # output - dict_items([('name', 'Prateek'), ('age', 21), (1001, 'Python'), (True, 'buses')       ('family', 'Goutam')])

# fromkeys() - creates a dictionary with specified keys, assigning same value to all the keys; default value is None
Dict = person.fromkeys([1, 2, 3], 'abc')
print(Dict)

# pop() - removes the key-value pair of the specified key
person.pop(True)

# popitem() - removes the last key-value pair 
person.popitem()

# clear() - empties the dictionary
person.clear()


print(person)