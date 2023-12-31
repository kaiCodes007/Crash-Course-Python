#A list of dictionaries

#Making a fleet of aliens
alien_0 = {'color': 'green', 'points': 20}
alien_1 = {'color': 'red', 'points': 30}
alien_2 = {'color': 'yellow' , 'points': 40}

#Creating a list of dictionaries
aliens = [alien_0,alien_1,alien_2]

for alien in aliens :
	print(alien)

#More suitable approach using range() function
#Make an empty list of the aliens
aliens = []
#make 30 green aliens
for alien_number in range(30) :
	new_alien = {'color': 'green', 'points': 50}
	aliens.append(new_alien)
print(alien)	

#Showing first five aliens
for alien in aliens[:5] :
    print(alien)
print('...')
#printing the number of the aliens created
print(f"The total number of the aliens created is : {len(aliens)}") 

#The aliens created have the same characteristics but python allows us to modify each element idividually
#Changing the colors for the first 3 aliens

for alien in aliens[:3] :
	if alien['color'] == 'green' :
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

#Showing the first five aliens again
for alien in aliens[:5] : 
    print(alien)
print('...')    
#This was a basic about putting dictionaries inside a list


#Now... Lets dive into puttting a list inside a dictionary

#store informattion about the pizza thats being discovered
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','pepperoni','extra cheese']
}
#Summarizing the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:" )
for topping in pizza['toppings']:
	print(topping)
print('...')	

#If a person could choose multiple languages in the previous example of this chapter
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['C'],
	'edward': ['python', 'perl'],
	'phil': ['js','brainfuck'],
}	
for name, languages in favorite_languages.items():
	print(f"{name.title()}'s favorite languages are:")
	for language in languages : 
		print(f"\t{language.title()}")
#The more refined version of above program could be:(ie checking if a user has polled multiple languages or not using if statement and len() function)
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['C'],
	'edward': ['python', 'perl'],
	'phil': ['js','brainfuck'],
}	
for name, languages in favorite_languages.items():
	if len(languages)>1:
		print(f"{name.title()}'s favorite languages are:")
		for language in languages : 
			print(f"\t{language.title()}")
	else:
	    print(f"{name.title()}'s favorite language is {languages[0]}")	
print('...')	


#A dictionary inside a dictionary
#While storing a number of users for a website, we can user their usernames as the keys and the information related to them as as the values, where the value is also a dictionary
users={
	'aeinstein': {
	    'first': 'albert',
	    'last' : 'eintstein',
	    'location': 'princeton',
	},
	'mcurie':{
	    'first' : 'marie',
	    'last' : 'curie',
	    'location': 'paris',
	},
}
for username , user_info in users.items():
	print(f"Username: {username}")
	print(f"\tFull name: {user_info['first'].title()} {user_info['last'].title()}")
	print(f"\tLocation: {user_info['location'].title()}")
