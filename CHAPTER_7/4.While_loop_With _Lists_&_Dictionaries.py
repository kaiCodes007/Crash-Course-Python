#Moving items from one list to another:Conforming or Verifying the users of an website ...
unconfirmed_users = ['alice','brian','candice'] 
confiremd_users = [ ]
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confiremd_users.append(current_user)
print("\nThe confirmed users are: ")
for user in confiremd_users : 
    print(f"\t{user}")
print('')    

#This method has potential issues because the length of the list changes dynamically with each pop()
#Using for loop for the same process
unconfirmed_users = ['jen', 'sarah', 'edward']
confirmed_users = []
for i in range(len(unconfirmed_users)):
    current_user = unconfirmed_users.pop(0) 
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

	
print('\nThe confirmed users are : ')    	
for user in confirmed_users:
    print(f"\t{user}")


#Removing all instances of specific values from a list

pets = ['dog','cat','dog','goldfish','cat', 'rabbit','cat'] 
print(f"\n{pets}\n") 

while 'cat' in pets :
    pets.remove('cat') 
print(pets) 



#Filling a dictionary with user inputs:

#A pollng program:
#Defining an empty dictionary
responses = {}

#Setting a flag to indicate that the polling is active:
polling_active = True

while polling_active:
	#prompting for input
	name = input("Whats your name? ")
	response = input("Which mountain would you like to climb? ")

	#Storing the response:
	responses[name] = response

	repeat = input("Is there another person to respond? ")
	print('')
	if repeat.lower() == 'no':
		polling_active = False

for name , response in responses.items():
    print(f"{name.title()} would like to climb Mt.{response.title()}")		