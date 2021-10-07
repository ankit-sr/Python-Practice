# print('This is list py')
# A list is a structure in python which can store any number of elements of different data types
# such as number, string, boolean, another list, tuples, dictionary, objects, etc.
# For example list = [10, 'name', False, True, [45, 56], ]

names = ['ankit', 'prateek', 'sushant']

age = [10, 55, 20, 25]

# Accessing list elements one by one
print(names[0] + names[1] + names[2] ) # names[3] - IndexError: List index out of range

# Common list methods
# append() takes one argument and inserts the element at the end of the list
names.append('vardhan') # Appending one element
names.append(['mishra', 'harmoine', 'harry']) # Appending a list


# insert() - is used to add an element to the list at specific index
# therefore, it takes two parameters, (index and element)
names.insert(2, "will")


# we can extend an iterable such as list, tuples to the current list using extend()
names.extend(age)


# count() - returns the number of time the given element is present in the list
print(names.count(15))


# sort() - sort the list in ascending order
# sort() is not supported when list contains elements of more than one data type
age.sort()
print(age)


# copy() - copies the the list to another list
age = names.copy()
print('age is : ' +  str(age))


# index() - returns the index of the element in the list, else gives ValueError: element not in the list
print(names.index('vardhan'))


# remove() - removes the specified element from the list
names.remove('will')


# pop() - removes the last element of the list
names.pop()

# clear() - empties the list
names.clear()

print(names)



''' 
    We can also create 2-D lists, where each element of a list is a list itself.
'''

people = [
    ['Prateek', 'Sushant', 'Vardhan'],
    ['Goutam', 'Gaurav', 'Rajput'],
    [21, 20]
]

print(people)

# accessing the elements - we use two square brackets
print( str(people[0][0]) +' '+ str(people[1][2]) +' '+ str(people[2][1]) )

# all methods discussed above are applicable on 2-D list

# using for-loop to access all list items one-by-one
# we are considering each list as a row, and each item in that list(row) as a col
for row in people:
    for col in row:
        print(col)