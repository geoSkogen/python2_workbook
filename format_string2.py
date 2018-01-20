x = "There are %d types of people." % 10 # grabs integer in string, assigns value or var
binary = "binary"
do_not = "don't."
y = "Those who know %s and those who %s" % (binary, do_not) # grabs strings  
# wthin a string, assigns values or vars to them per an array of arguments
# that follows their order of appearance in the string;

print (x)
print (y)


print ("I said: %r." % x)#grabs first statement and reprints it;
print ("I also said: '%s'." %y)

hilarious = False #sets var to grab with rchar
joke_eval = "Joke funny, No? %r"#adds rchar to string var

print (joke_eval % hilarious)# grabs both string var and rchar, evaluates

w = "This is the left side of . . . "
e = "a string with a right side, too."

print (w + e)
