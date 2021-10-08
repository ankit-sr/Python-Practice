'''
    We can perform write operation in a file using either a or w or r+ mode.
    a - allows us to append code at the end of the file
    w - overwrites the body of current file with the provided text. It also creates a new file if the file
        specified is not present.
'''

file = None

# using a (append mode)
try:
    file = open('sample.txt', 'a')

    print(file.writable())

    file.write('\nVardhan Singh Rajput')

except Exception as e:
    print(e)

finally:
    if(file is not None):
        file.close()
        print('append - File closed successfully')

# print(file)   # output - <_io.TextIOWrapper name='sample.txt' mode='a' encoding='cp1252'>

# using 'w' (write) mode

file = None
try:
    file = open('sample.txt', 'w')

    file.write('Prateek Goutam')

    file.writelines(['This is first line', 'This is second line', 'This is third line'])

    file.seek(offset)
except Exception as e:
    print(e)

finally:
    if(file is not None):
        file.close()
        print('write - File closed successfully')