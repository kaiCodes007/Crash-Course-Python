#Returning a simple value
def get_formatted_name(first_name,last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('kai','chhetri')	
print(musician)

#Making an argument optional: Sometimes it makes sense to make an argument optional so that people can provide information only when they want to
#This is done by setting a default value to that parameter ie an empty string
def get_formatted_name(first_name,last_name,middle_name = ""):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}\n"
	else:
	    full_name = f"{first_name} {last_name}\n"
	return full_name.title()    
print(get_formatted_name('john','hooker','lee'))
print(get_formatted_name(first_name = 'lionel',middle_name = 'andres',last_name = 'messi'))
#print(get_formatted_name('lionel','messi','andres')) if positional argments were used

print(get_formatted_name('stephen','hawking'))


#Returning a dictionary
def build_person(first_name,last_name):
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimmy', 'hendrix')
print(musician)

#Modification of above dictionary returnning code with the optional values like age and middle name

def build_person(first_name,last_name,middle_name = '',age = None):
	if middle_name:
		person = {'first':first_name,'middle':middle_name,'last':last_name}
	else:
		person = {'first':first_name,'last':last_name}

	if age:
	    person['age'] = age
	return person

     	

print(build_person('lionel','messi','andres',37))
print(build_person('stephen','hawking'))

#Using while loop in a function
def formatted_name(first_name,last_name):
	full_name = f'{first_name} {last_name}'
	return full_name.title()

while True:
	print("\nPleas tell me your name. (Enter q anytime to exit)")

	f_name = input("First name: ")
	l_name = input("Last name:")
	if f_name == 'q':
		break
	if l_name == 'q':	
		break
	name = get_formatted_name(f_name,l_name)	
	print(f"Hello, {name.title()}\n")

	
	

		
		
	

