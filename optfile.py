#read a file
from sys import argv

script, filename = argv

content1 = open(filename)

print("My file is %r:" % filename)
print(content1.read())

print("Type the filename :")
file_again = input("> ")

content2 = open(file_again)

print(content2.read())



#copy from one file to another
from sys import argv

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

input = open(from_file)
indata = input.read()

output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")

output.close()
input.close()
