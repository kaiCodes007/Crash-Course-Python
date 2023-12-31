#Make a list of people who should take part in favorite language poll.. Include some names that are already taken in the dictionary and some that are not
#Loop through the list of people who should take the poll .. if they have already taken the poll ,print a message thanking them for responding.
#If they have not yet taken the poll. print a message inviting them to take part at the poll

favorit_language={
	'kai': 'python',
	'jen' : 'R',
	'sarah': 'ruby',
	'rana' : '1X',
	'bhatte': 'react',
	'binayak': 'perl',
}
should_participate=['kai','cozmix','sandy','rana','ritesh','samman','pawan','bhatte','manish','binayak']

for user in should_participate :
	if user in favorit_language.keys() :
		print(f'Thanks Mr.{user.title()} for responding')
	else :
	    print(f'Mr.{user.title()} will be appreciated if he could take part in the poll.')	
print('')	    



#or we can also run loop in the dictionary and check if the key is in the list should_participate

for user in favorit_language.keys() :
	if user in should_participate :
		print(f"Thank you Mr.{user.title()} for responding")
	else :
	    print(f'It is kindly informed that Mr.{user.title()} is invited for the poll')	

print('')


"""The main difference between these two approach is that.. in first method python interpreter starts looking through list and then checks in the favorit_language 
dictionary if a person has or has not taken the poll..

In the second method, the interpreter scans for each key from the dictionary and then matches with the list, one at a time.... Although the outcome is same... The 
order of the result might be different.	  
"""  

#Printing the name of the person who likes 1X
for name, value in favorit_language.items():
	if value =='1X' :
		print(f"The person associated with the {favorit_language[name]} is {name}")
print('')	

#You can practice some other ideas too	