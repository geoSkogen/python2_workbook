#assign ordianl array of rchars to a var
formatter = "%r %r %r %r"
#pass arguments to the array
print (formatter % ("first", "second", "third", "fourth"))
print (formatter % (1, 1, 2, 3))

#pass arrays to the array to create 2 dimensional array
print (formatter % (formatter, formatter, formatter, formatter))
