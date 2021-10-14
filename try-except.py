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
# but the problem is we can never know the type of exception
# we can explicitly define the except block for specific error

try:
    # a = 10/0
    x = int(input('Enter the value : '))
    print(x)

except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)

except Exception as e:
    print(e)     # we can still define an except block for all errors


# the user can himself raise an exception in certain conditions 
# using 'raise' keyword.

try:
    x = int(input('Enter the value : '))
    if(x < 0):
        raise Exception('The number can not be negative')
    print(x)

except Exception as err:
    print(err)