''' Like lists, tuples are a structure in python than can contain more than one element of
    diferent data types. But, tuples are immutable, that means a tuple value can only be assigned once
    and remains, intact during the execution of program.

    That means, that we can only access (read-only mode) the elements of the tuple, but can not change it
    on our convenience.
'''

names = ('ankit', 'prateek', 'sushant' , 12 , True, False, ['abc', 24], (15, 8))

# accessing elements of tuples using their indexes
print(names[0] + names[1] + names[2])

# count() - returns the number of time the given element is present in the tuple
print(names.count('prateek'))

# index() - returns the index of the element in the tuple, else gives ValueError: element not in the tuple
print(names.index(True))
