'''
    Write a program to create a file called sample.txt in your computer . 
    Now ask the user to type a message and write it in the file . 
    Finally display how many capital letters, how many small letters , how many digits and how many special characters were written in the file.
    Also properly handle every possible exception the code can throw
'''

file = None

try:
    file = open('sample.txt', 'w')

    message = input('Enter message to write in the file : ')

    file.write(message)

    upper = lower = digits = specialchars = 0
    for ch in message:
        if 65 <= ord(ch) <= 90:
            upper += 1
        elif 97 <= ord(ch) <= 122:
            lower += 1
        elif 48 <= ord(ch) <= 57:
            digits += 1
        
    print('Upper: ', upper)
    print('Lower: ', lower)
    print('Digits: ', digits)

except FileNotFoundError as e:
    print('Could not locate file.')

except OSError as e:
    print('Error while writing the message to the file.')

finally:
    if file is not None:
        file.close()


