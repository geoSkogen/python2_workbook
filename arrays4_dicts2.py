states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI',
}

cities = {
   'FL': 'Jacksonville',
   'CA': 'San Francisco',
   'MI': 'Detroit',
}

cities['OR'] = 'Portland'
cities['NY'] = 'New York'

print ('-' * 10)

print("an Oregon city: ", cities['OR'])
print("a New York city: ", cities['NY'])

print ('-' * 10)

print("abbreviation for Florida: ", states['Florida'])
print("abbreviation for Michigan: ", states['Michigan'])

print ('-' * 10)

for state, abbrev in states.items():
    print("%s is abbreviated a %s" % (state, abbrev))

print ('-' * 10)

for abbrev, city in cities.items():
    print("%s  is located in %s" % (city, abbrev))

print ('-' * 10)

#this statement makes use of the primary-key/foreign-key structure of our two dicts
for state, abbrev in states.items():
    print("%s in abbreviated %s and is home to %s" % (state, abbrev, cities[abbrev]))

print ('-' * 10)

#find a way to do this without hard-coding the data
state = states.get('Texas')

if not state:
    print("sorry; no Texas")

city = cities.get('TX','does not exist')
print("city located in 'TX': %s" % city)
