"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value
as they enter each toppings print message saying you;ll add that topping to their pizza
"""
requested_toppings = []
prompt = "Please enter the pizza toppings .. Ill enter them to the requestedtoppings"
prompt += "\nEnter 'quit' to exit: "
message = ''
while message != 'quit':
	message = input(prompt)
	if message != 'quit': 
		print(f"Adding {message}\n")
		requested_toppings.append(message)
print("The toppings you have requested are: ")		
for toppings in requested_toppings: 
    print(f"\t{toppings}")
  

#Excercise movie ticket
age = input("Enter your age :")
age = int(age)

if age < 3:
	print("The ticket is free\n")
elif age >= 3 and age <= 12 :
	print("The ticket is $10 only")
else : 
    print("The ticket is $15 only")	


#Excercise: The Three Exits
#First one using a conditional test in while loop (which i already applied on the first one)
#Second one using an active variable
prompt = "You can enter 'quit' or 'exit' to finish anytime"
prompt += "\nCan we start with your name please?: "
prompt1 = "Enter Your Favorite place: "
places = { }
active = True
while active:
	name = input(prompt)
	if name.lower() == 'quit' or name.lower() == 'exit':
		active = False
	else:
		place = input(prompt1)
		if place.lower() == "quit" or place.lower() == "exit":
			active = False
		else :
			print(f"{place.title()}, An exceelent choice indeed , {name.title()} \n")
			places[name] = place 	

print(f"\n{places}")


#Third One: Using a break statement
prompt = 'Enter Your Favorite actors:'
prompt += "\nPress exit or quit anytime to finish: "
while True:
	actor = input(prompt)
	if actor.lower() == 'quit' or actor.lower() == 'exit':
		break
	else:
	    print(f"{actor.title()}, Seems like we have similar choices")	


"""A never ending loop
x = 1
while x <=5 :
	print(x)
	x += 1 
	#The omission of the last incremental line makes this loop run forever
	"""	

