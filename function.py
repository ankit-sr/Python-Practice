'''
    Using functions to acheive a particular task is a way to avoid code redundancy.
    We can use functions in python to complete a particular task any number of times,
    just by calling the name of that function in our code.
'''

# we define function using a keyword 'def' followed by function_name and ':'
def printHello():
    print('Hello')


printHello()  # calling the function

# we can also pass parameters to the function, to improve its functionality
def printName(name):
    print('Hello! I am ' + name)

printName('Prateek')    # calling the function with parameters, we can pass as many parameter we want

# function is not only used to print something, infact they can return a value
# below function increases a number by ten, and returns it
def increaseAge(age):
    return age+10

age = 15
newAge = increaseAge(age)
print(newAge)

# even a function can return more than one element
def capitalizeNameIncreaseAge(name, age):
    name = name.upper()
    age = age + 10

    return name, age

name = 'Ankit'
age = 20
name, age = capitalizeNameIncreaseAge(name, age)
print(name + " " + str(age))