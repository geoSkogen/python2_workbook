import os

newfile = open("rename_me.txt", "w+")
newfile.write("I am with name")
newfile.close()

os.rename("rename_me.txt", "i_am_renamed.txt")

nextfile = open("i_am_renamed.txt", "r+")
sample = nextfile.read()
print(sample)
nextfile.close()

os.remove("i_am_renamed.txt")
