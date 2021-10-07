'''
    We can manage files in python.
    A file can be opened in 4 modes : r - read,
    w - write, a - append and r+ - read and write

    while managing files, keep in mind to open the correct file and
    also close the file.
'''

'''
    we should not use read() with readlines() because, when either of the function is called
    the cursor in the file, moves to the end of file (EoF), therefore either one of them will be executed
    whichever is written first.
'''
file = None
try:
    file = open('README.md', 'r')

    print(file.readable())  # returns true or false, whether we can perform read operation or not

    # print(file.read())      # reads whole file in bunch
    # x = file.read()
    # print( type(x))       # output - <class 'str'>

    print(file.readline())  # reads single line at a time

    # print(file.readlines())  # returns a list of lines in file   

    # using for-loop and readlines() to print each line of the file
    for line in file.readlines():
        print(line)

except exception as e:
    print(e)

finally:
    if file is not None:
        file.close()    # closing file in necessary
        print('File closed successfully')