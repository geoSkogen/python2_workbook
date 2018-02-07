import os

'''
fl = open("famines_lamp.txt", "r+")

print ("filname is: %s" % fl.name)
print ("file is closed: %s" % fl.closed)
print ("file was opened in %s mode" % fl.mode)
print ("softspace?: %s" % fl.softspace)

fl.close()
'''

'''
newfile = open("pythonic.txt", "w")
newfile.write("\r\nI am the maelstrom's deafening song\r\nThe ether through which the fallen descend\r\n")
newfile.close()
print "wrote this file: pythonic.txt"

oldfile = open("pythonic.txt", "r+")
newstr = oldfile.read()
print newstr
print ("current file position is: %i" % oldfile.tell() )
oldfile.seek(0,0)
print ("current file position after .seek(0,0) is: %i" % oldfile.tell() )
oldfile.seek(19,0)
newstr = oldfile.read()
print ("read file after .seek(19,0):\r\n")
print newstr
oldfile.seek(0,0)
oldfile.write("\r\nI am Homer Simps")
oldfile.seek(0,0)
newstr = oldfile.read()
print ("read file after .seek(0,0) and overwrite:")
print newstr
oldfile.close()
'''

'''
os.rename("deaths_mistress.txt","famines_lamp.txt")
newfile = open("famines_lamp.txt","r")
newstr = newfile.read()
print("\r\nopened %s:\r\n\r\n%s" % (newfile.name, newstr) )
newfile.close()
os.rename("famines_lamp.txt", "deaths_mistress.txt")
oldfile = open("deaths_mistress.txt","r")
newstr = oldfile.read()
print("renamed %s:\r\n\r\n%s" % (oldfile.name, newstr) )
oldfile.close()
'''
