from sys import argv

script, filename = argv

txt= open(filename)
print ("your file:\n %r" % filename)
print (txt.read())
txt.close()

print ("enter a filename:")
file_again = raw_input("> ")
txt_again = open(file_again)
print (txt_again.read())
txt_again.close()
