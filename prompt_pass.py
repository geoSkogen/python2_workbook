from sys import argv

script, user_name = argv
prompt = "> "

print ("Hello %s, I am the %s script" % (user_name, script))
print ("please enter your password")
pswrd = input(prompt)
print ("your password is seriously %r?" % pswrd)
