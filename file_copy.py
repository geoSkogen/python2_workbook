from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("copying from %s to %s" % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("input file is %d bytes long" % len(indata))
print("output file exists: %r" % exists(to_file))
print("copy now?\n --hit ENTER to copy --hit CTRL + C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("success")

out_file.close()
in_file.close()
