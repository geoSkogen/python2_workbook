from sys import argv

script, name = argv

num = raw_input("Well, hello, %r. How many today?" % name)
strnum = str(num)
print strnum, " it is!"
