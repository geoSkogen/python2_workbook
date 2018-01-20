import re

phone1 = "456-789-1011 #this is a python style comment"
phone2 = "(124) 125-9999 #this is a python style comment"
phone3 = "098.765.4321 #this is a python style comment"
print(phone1)
print(phone2)
print(phone3)
#this will remove all python style comments
num1 = re.sub(r'#.*$', "", phone1)
num2 = re.sub(r'#.*$', "", phone2)
num3 = re.sub(r'#.*$', "", phone3)
print(num1)
print(num2)
print(num3)

#this will remove all non-digits
digs1 = re.sub(r'\D', "", num1)
digs2 = re.sub(r'\D', "", num2)
digs3 = re.sub(r'\D', "", num3)
print(digs1)
print(digs2)
print(digs3)
