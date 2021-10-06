'''
    Conditional statements controls the flow of execution of a program based on the provided criteria/condition
    We have, if-else in python as conditional statement.

    Note : Pyhton does not support switch-case

    The flow of the if-else goes like : 
        if the condition provided is met (True), then the code written inside the if-statement gets executed
        otherwise, the code written inside the else-statement gets executed.
'''

a = 5 
b = 6 
c = 8

# using only if statement
if(a < b) :
    print('b is greater than a')


# using if-else statement
if(a > b) :
    print('a is greater than b')
else:
    print('b is greater than a')


# using if else-if or elif
if(a > b) :
    print('a is greater than b')
elif(a > c):
    print('a is greater than c')
else:
    print('a is lesser than b and c')






