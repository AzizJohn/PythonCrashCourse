alien_0 = {} # an empty dictionary
alien_0['color'] = 'green' # add a new key-value pair
alien_0['points'] = 5
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0['color']) # green
print(alien_0['points']) # 5
alien_0['color'] = 'yellow' # change values in a dictionary
del alien_0['points'] # remove a key-value pair
languages = { # This is a recommended format. It's not compulsory, 
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',  # use a comma for the last key-value pair as well.
	}
language = languages.get('Tom', 'person not found')
#The first argument is the key to be searched
#The second argument is the value to be returned if the key doesn't exist.
#The second argument defaults to the value None

for person,language in languages.items():
	print(f"\nPerson: {person}")
	print(f"Language: {language}")
#the method items() returns a list of key-value pairs.

for person in languages.keys():
	print(person)
#The following has the same result.
for person in languages:
	print(person)
	
'erin' not in languages.keys() # True. The keys() method returns a list of keys

for language in languages.values():
	print(language)
#The values() method returns a list of values without any keys.
#It doesn't check repetition.

for language in set(languages.values()):
	print(language)
#A set is a collection in which each item must be unique.

languages = {'python', 'ruby', 'python', 'c'}
# You can build a set directly using braces and separating the elements
# with commas.
print(languages) # {'ruby', 'c', 'python'}

aliens = []
#Make 30 green aliens.
for alien_number in range(30):
	new_alien = {
	'color': 'green',
	'points': 5,
	'speed': 'slow',
	}
	aliens.append(new_alien)
