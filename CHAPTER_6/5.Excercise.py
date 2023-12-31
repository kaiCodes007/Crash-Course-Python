#Store three dictionaries in a list .... and print them using loop
people_0 = {'first': 'kai', 'last': 'chhetri' , 'age' :23, 'city': 'kirtipur'}
people_1 = {'first': 'samman', 'last': 'basnet', 'age': 22, 'city': 'lalitpur'}
people_2 = {'first': 'sushil', 'last' : 'bhatte', 'age': 21, 'city': 'bhaktapur'}

people_list = [people_0,people_1,people_2]
for people in people_list:
	#Either we can print them as a dictionary:
	print(people)
    #Or in a more meanigful manner
	print(f"FullName: {people['first'].title()} {people['last'].title()}")
	print(f"Age: {people['age']}")
	print(f"City: {people['city'].title()}")
	print('...')



#Actually the question meant the other way ..s0o
people_0 = {'fname': 'kai', 'lname': 'chhetri' , 'age' :23, 'city': 'kirtipur'}
people_1 = {'fname': 'samman', 'lname': 'basnet', 'age': 22, 'city': 'lalitpur'}
people_2 = {'fname': 'sushil', 'lname' : 'bhatte', 'age': 21, 'city': 'bhaktapur'}

people_list = [people_0,people_1,people_2]
for people in people_list:
	for key,value in people.items(): 
		print(f"{key}: {value}")
	print('')

#Another
"""Make several dicionaries ,where each dictionary represents a different pet.In each dicionary ,
include the kind of animal and the owner's name .Store these dicionaries in a list called pets. Next
loop throug your list and as you do, print everything you know about each pet"""

pet_0 = {'type': 'dog','name': 'jack','owner': 'cozmix'}
pet_1 = {'type': 'cat', 'name': 'bill', 'owner': 'kai'}
pet_2 = { 'type': 'rat', 'name': 'chuck', 'owner': 'keshav'}

pets = [pet_0,pet_1,pet_2]
for pet in pets: 
	for key, value in pet.items(): 
		print(f'{key} : {value}')
	print('')
print('')	

#A different approcah may be ... using only one for loop and using dicionary access method on keys while printing
for pet in pets:
	print(f" {pet['name'].title()} is a {pet['type'].title()} owned by {pet['owner'].title()}\n")



"""Make a dictionary called favorite_places. Think of three names to use as keys in the dicionary
and store one to three favorite places for each person .. Loop through the dicionary and print each person's name and favorite placess"""

favorite_places = {
	'jen': ['paris','kathmandu','istanbul'],
	'sarah': ['pokhara', 'delhi', 'toronto'],
	'edward': ['bandipur','moscow', 'bangkok'],
}

for person ,places in favorite_places.items():	
	print(f"The favorite places of {person.title()} are:")
	for place in places:
		print(f"\t{place.title()}")
	print(' ')	



"""Favorite-Numbers:Modifiy your previous program of favorite_numbers so each person can have more than one favorite number
Then print each person's name with his/her favorite number\
"""

favorite_numbers = {
	'kai' : [10],
	'sandy': [9,30],
	'rana' : [10,30]
}
for name, numbers in favorite_numbers.items(): 
	if len(numbers)>1: 
		print(f"{name.title()}'s favorite numbers are:")
		for number in numbers: 
			print(number)
		print('')	
			
	else:
	    print(f"{name.title()}'s favorite number is :")	
	    print(f"{numbers[0]}\n")

#for printing the name of the people who participated in the favorite no poll
print('The people who participated are:')
i=0
for keys in favorite_numbers.keys() : 
	print(keys)
	i=i+1
print(f"\nAs you can see , the total no of people who participated were: {i}\n")


"""Make a dicionary called lists: Use the name of three cities as the keys in your dictionary.Create a dictionary of 
information about the each city by including the country that the city is in , its approximate populationa and a fact about that city
.Print the name of the each city and the information you have stored about it
"""
cities = {
	'kathmandu': {
	    'country': 'nepal',
	    'apopulation': 5_000_000,
	    'fact': 'city of temples',
	},
	'paris': {
	    'country':'france',
	    'apopulation': 30_000_000,
	    'fact': 'city of lights',
	},
	'bangkok': {
	    'country': 'thailand',
	    'apopulation': 20_000_000,
	    'fact' : 'city of angels',
	},

}
print("The cities and their respective information are:\n")
for name, city_info in cities.items():
	print(f'{name.title()}:')
	for key, info in city_info.items():
		print(f"\t{key.title()} : {info}")
	print('')	


#A different approach can be:
for name,city_info in cities.items():
	print(f"The fact's of city {name.title()} are:")
	print(f"\tThe city lies in country {city_info['country'].title()}")
	print(f"\tIt has an  approximate population of {city_info['apopulation']}")
	print(f"\tAnd it is also known as {city_info['fact'].title()}")
	print('')

    
#Adding some new cities
cities['sydney']={
	'country': 'australia',
	'apopulation': 15_000_000,
	'fact': 'the harbour city',
}
cities['dubai']= {
	'country': 'united arab emirates',
	'apopulation': 2_000_000,
	'fact': 'the city of gold',
}
print(cities)
print('')

#Changing  a value inside and adding a new one 
for city, city_info in cities.items():
	if city== 'kathmandu':
		city_info['fact']= 'city of living goddess'
		#city_info['fact2'] ='balen city'   (you can change it back to the line of code when you want... you know how to do it)
print(cities)		

for city,city_info in cities.items():
	print(f"The facts of city {city.title()} are:")
	for key, value in city_info.items():
		if key == 'country':
			print(f"\tIt lies in {key} {value.title()} ")
		if key == 'apopulation': 
			print(f"\tThe approximate population is {value}")
		if key == 'fact': 
		    print(f"\tIt is also known as {value.title()}")

	print('')	    		    

#The code from line 157-167 can be considered as a improvised version of the code from 128-133. Even though both the outputs are same but the latter one wins from a logical view





    
