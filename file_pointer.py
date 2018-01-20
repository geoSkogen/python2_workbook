fileobj = open("file_pointer.txt", "r+")
sample = fileobj.read(13)
print("first 13 bytes: %s" % sample)

pos = fileobj.tell()
print("position: %s" % pos)

newpos = fileobj.seek(13, 0)
newsample = fileobj.read(10)
print("bytes 13 - 23: %s" % newsample)

fileobj.close
