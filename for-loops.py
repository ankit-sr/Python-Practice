'''
    for-loops are another kind of loop to iterate over certain collection or to repeat some code for a certain number of times.
'''

# using for loop for collections such as a string or list

for char in 'this is a string':
    print(char)

friends = ['prateek', 'sushant', 'mishra']

for friend in friends:
    print(friend)

# using range() in for-loop
# if we pass only one parameter, it is considered as upper limit and ranges from 0 to x
for i in range(10):     # here 10 is not included
    print(i)

# providing two parameters in range() specifies the starting(included) and ending (excluded) of the range
for i in range(3, 8):
    print(i)

# range() can take upto 3 parameters, the third one is the step value, i.e. by how much you want to increase the value 
# in the next iteration
for i in range(3, 8, 2):
    print(i)