'''
    Write a program to ask the user to input 2 integers and calculate and print their division. Make sure your program behaves as follows:

    If the user enters a non integer value then ask him to enter only integers
    If denominator is 0 , then ask him to input non-zero denominator
    Repeat the process until correct input is given

    Only if the inputs are correct then display their division and terminate the code

'''

#Solution

while(True):
    try:
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        if num1 <= 0 or num2 < 0:
            raise Exception('Negative numbers are not allowed')
        res = num1 / num2
        print(res)
        break
    except ValueError as e:
        print("The numbers should be integers only")
    except ZeroDivisionError as e:
        print("The denominator (number 2) can not be zero")
    except Exception as e:
        print(e)