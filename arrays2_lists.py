ten_things = "airplane puppet orange spoon window"
print("ten things; ", ten_things)
print("there aren't ten things on this list")
stuff = ten_things.split(' ')
more_stuff = ["frog", "spider", "star", "moon", "shingle"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("adding: ", next_one)
    stuff.append(next_one)
    print ("length: %d items" % len(stuff))

print("full list: ", stuff)
print("second elm: ", stuff[1])
print("last elm: ", stuff[-1])
print("pop last elm: ", stuff.pop())
print("join on spaces to make a string:")
print (' '.join(stuff))
print("join on hashes, 4th & 5th elms:")
print ('#'.join(stuff[3:5]))
