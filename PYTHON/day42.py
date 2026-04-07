#--------------file handling note--------------------#

# file handling is a way to store data in a file and read it later
# we can use the open() function to open a file and read or write data to it
# the open() function takes two arguments: the file name and the mode (r for read, w for write, a for append)
# we can use the read() method to read the contents of a file and the write() method to write data to a file
# we can also use the with statement to automatically close the file after we are done with it
# example of writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a file handling example.\n')
    file.write('We can write multiple lines to the file.\n')
# example of reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)