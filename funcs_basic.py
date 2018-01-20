def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

def print_two2(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print ("arg1: %r" % arg1)

print_two("geoseph","Skogen")
print_two2("geoseph","Skogen")
print_one("geoseph")
print_one("Skogen")
