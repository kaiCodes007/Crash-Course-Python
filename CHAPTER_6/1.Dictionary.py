#A simple dictionary that stores information about a particular alien
alien_0={'color': 'green', 'points': 10}
print(alien_0['color'])
print(alien_0['points'])

#Working with dictionaries
#Accessing values in a dictionary
print(f"You earned {alien_0['points']} by defeating the alien with color {alien_0['color'].upper()}\n")

#Adding new key-value pairs
#adding x and y co-ordinates for the alien
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('')

#modifying values:
alien_0={'color': 'red'}
print(f"The alien is {alien_0['color']} in color")

alien_0['color'] = 'yellow'
print(f"\nThe alien is now {alien_0['color']} in color\n")

#A more interesting example...lets track the position of an alien that can move at different speeds
alien_0={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"The original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
	#This must be a fast alien
    x_increment = 3

alien_0['x_position']=alien_0['x_position'] + x_increment
print(f"The new position : {alien_0['x_position']}\n")

#Removing key-value pairs
print(alien_0)
print('Removing speed key-value pairs...')

del alien_0['speed']
print(alien_0)

"""
Assigning a new key-value pair
alien_0['laugh']= 'smile'
print(alien_0)

Modifying the newly added key-value pair
alien_0['laugh'] = 'cry'
print(alien_0)\
"""

#A dictionary of similar objects
favorite_languages={
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}
print(favorite_languages)
print(f"\nThe favorite language of Phil is {favorite_languages['phil'].upper()}\n")

"""Using get()method to access values:
Using keys in the square bracket to access a key value might result to one potential problem:if the
key value doesnt exist , the traceback will throw a KeyError....

print(f"\nThe favorite language of Phil is {favorite_languages['kai'].upper()}\n")

The above code will throw an error..
So we use get() method to set a default value to be returned if the key doesnt exist
"""

print(f"The favorite language of Kai is {favorite_languages.get('kai','No language assigned')}")
#Even though there's no language assigned... python wont throw an error this time and returns a default value set instead

#We can also assign the value obtained to a variable and then display it
print(alien_0)
points_got=alien_0.get('points','No value assigned')
print(points_got)


#Excercise
#Create a dictionary to store info about a person and then print each piece of info

person_info={'first_name': 'kai', 'last_name': 'chhetri', 'age': 23, 'city': 'kathmandu'}
print(f"The first name of the person is {person_info['first_name'].upper()}")
print(f"The last name of the person is {person_info['last_name'].upper()}")
print(f"The age of the person is {person_info['age']}")
print(f"The address of the person is {person_info['city'].upper()}\n")


#Create a dictionary to store peoples favorite number ... Print each persons name and their fav_nos
favorite_numbers={
	'kai': 10,
	'samman': 8,
	'arbin': 7,
	'bhatte': 11,
	'sandip': 9,
    }
print(f"The favorite number of kai: {favorite_numbers['kai']}")
print(f"The favorite number of samman: {favorite_numbers['samman']}")
print(f"The favorite number of sandop: {favorite_numbers['sandip']}")
print(f"The favorite number of ritesh: {favorite_numbers.get('ritesh','Oops! No number assigned')}\n")

#Create five programming words you have learned till now
prog_words={
	'print()':'Print the statement',
	'append()': 'Add a new value to a list',
	'insert()': 'Insert a new value to the list at a particular index',
	'del': 'Delete a value from the list using its index and delete a key-value pair from dictionary using the key value',
	'pop()': 'Popping a value from the list either or not using index',
	'remove()': 'Remove a value form the list using its value attribute rather than index itself',
	'sort()': 'Sort a list permanently',
	'sorted()': 'Sort a list for temporary purpose',
	'reverse()': 'Print the list in a horizontal reverse manner',
	'len()': 'Calculate the no of value items in a list',
	'range()': 'Create a list by specifying a range:range(start),range(start,stop) and range(start,stop,step) ',
	'list()': 'Creating a list directly using range() function',
	'get()' : 'Return a default set value when the key item doesnt exist rather than producing a KeyError'



}
print(prog_words)
#print each value by using the key along with the key itself,.....








