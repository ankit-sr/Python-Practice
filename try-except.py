'''
    Exception Handling in Python is achieved using "try-except" block where
    we write our possible exception throwing code in the "try" block and
    the code to be executed after catching error in "except" block. 
'''

try:
    # a = 10/0
    x = int(input('Enter the value : '))
    print(x)

except:
    print('Invalid input')

# the above except, handles all types of exceptions and will execute same code
# we can explicitly define the except block for specific error

try:
    a = 10/0
    x = int(input('Enter the value : '))
    print(x)

except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)

except:
    print('some error occured')     # we can still define an except block for all errors