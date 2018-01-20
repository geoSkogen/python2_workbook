import re
#line = "503-10-1212"
#searchObj = re.search( r'^([\d]{3})')

line = "apples are bigger than grapes"
searchObj = re.search( r'(.*) are (.*?) than (.*)', line, re.M|re.I)
if searchObj:
    print(searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))
    print(searchObj.group(3))
else:
    print("whatup python")
