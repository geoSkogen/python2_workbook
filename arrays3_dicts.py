obj = {'length': '3:36', 'listens': '56', 'genre': 'metal', 'playlist': 'demos'}
print(obj['listens'])
print(obj['playlist'])
print(obj['genre'])
print(obj['length'])

obj[0] = "Acolytes"
obj[4] = "BITreCordings"

print(obj)

del obj[4]
del obj['genre']
print(obj)
