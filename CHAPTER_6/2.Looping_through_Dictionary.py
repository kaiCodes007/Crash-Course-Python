#Looping through all key-value pairs
#lets consider a new dictionary that stores information about a user on a website
user_0={
	'username': 'kai',
	'first': 'asmit',
    'last': 'chhetri',
}
for key, value in user_0.items():
	print(f'\nKey:{key}')
	print(f'Value:{value}')
print('')

#This loop is particularly useful on the following case: 
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
	'get()' : 'Return a default set value when the key item doesnt exist rather than producing a KeyError',


}
for method, elaboration in prog_words.items():
	print(f'method : {method}')
	print(f'Elaboration: {elaboration}')


#Looping through all the keys of the dictionary using keys() method
favorite_languages={
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in favorite_languages.keys() :
	print(name)
print('')	

#The looping through the keys is actually the default behavior when looping through dictionary
#So the following loop will produce the same output as upper loop	
for name in favorite_languages:
	print(name.upper())

#Now lets print a message to a couple of friends about the languages they chose
#We'll loop through the dictionary as we did previously...
#But when the name matches one of our friends... we'll display a message
#favorite_languges={......}	
friends=['phil','sarah']
for name in favorite_languages.keys() :
	print(f'Hi {name.title()}.')

	if name in friends:
		#Either we can assign a variable 'language' as shown in comment below or directly extract the value in the same line .. (by accessing through the key value in dictionary)
		#language=favorite_languages[name].title()
		print(f'{name.title()}, I see you love {favorite_languages[name].title()}\n')

#We can also use the keys()	method to find out if a particular person was polled	
if 'erin' not in favorite_languages.keys():
	print("Erin... you might wanna take a poll\n")
	

#looping thorough a dictionary in different order
for name in sorted(favorite_languages.keys()) :
	print(f'Hi {name.title()}.. Thank you for taking the poll')

#Looping through all values in a dictionary
print("\nThe selected languages are:")	
for value in favorite_languages.values() :
	print(value.title())

#In sorted manner
print("\nThe selected languages in sorted order are:")	
for value in sorted(favorite_languages.values()):
    print(value.title())
print('')    

#For avoiding the repetition of entities
for language in set(favorite_languages.values()) :
	print(language.title())
print('')	

#With sorted function
for language in set(sorted(favorite_languages.values())) :
	print(language.title())
print('')	


#Excercise:Glossary with the methods you have learnt till now and print key-value pairs
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
	'get()' : 'Return a default set value when the key item doesnt exist rather than producing a KeyError',
    'item()': 'Return the both key-value pair from the dictionary by looping',
    'keys()': 'Return all the keys by looping',
    'values()': 'Return all the values by looping ',
    'set()' : 'Return the non repeated values as in a set from dictionary'

}

for method, description in prog_words.items() :
	print(f'\nMethod: {method}')
	print(f'Description: {description}')

print('')	

#A dictionary containg three major rivers and the country
river_origins={
	'nile':'egypt',
	'amazon':'brazil',
	'karnali':'nepal',
}
for river,country in river_origins.items() :
	print(f'The {river.title()} runs through {country.title()}')

print('')	

#A loop to print the name of the each river included in the dictionary
for river in river_origins.keys() : 
	print(river.title())
print('')	

#A loop to print the name of the river in sorted order along with set method
for river in sorted(set(river_origins.keys())) :
	print (river.title())
print('')	

#A loop to print the name of the each country included in the dicrionary
for country in river_origins.values() :
	print(country.title())
print('')	

#A loop to print the name of the countries in sorted manner along with set method
for country in sorted(set(river_origins.values())) :
	print(country.title())
print('')


