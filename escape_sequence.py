tabbed = "\tI'm tabbed-in."
split = "I'm split\non a line."
escape_slashes = "I'm \\ just \\ a \\ boring \\ old \\ orange."

listy = """
basic chaotic listy:
\t* feta cheese
\t* viagra
\t* beef bones\n\t
\t* sleepytime tea
"""

arr = "%s %s %s %s"

print(tabbed)
print(split)
print(escape_slashes)
print (listy)

#I want to know why this loop doesn't work
#python tells me I'm trying to convert an integer to a string
#but I'm not doing that
"""i = 0
while i < 14:
    for i in ["/","-","|","\\","|"]:
      print("%s\r" % i)
      i += 1"""

#I figured out why following code didn't render correctly:
#the array was made of rchars instead of strings
print(arr % (tabbed + "\n", split + "\n", escape_slashes, listy))
