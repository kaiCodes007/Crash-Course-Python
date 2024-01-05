#Passing a list inside a fucntion
def greet_users(names):
	for name in names:
		message = f"Hello {name.title()}"
		print(message)

usernames = ['hanna', 'margot', 'angelina']
greet_users(usernames)

#Modifying a list 

#Without using a function
unprinted_designs = ['phone case','robot pendant', 'dodecahedron']
completed_models = [ ]

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"\nPrinting model : {current_design}")
	completed_models.append(current_design)

print('\nThe completed models are: ')
for completed_model in completed_models :
    print(completed_model)

print('')    	


#Using a function: We use two differnet functions for two specific tasks

def print_models(unprinted_models, completed_designs):
	while unprinted_models:
		current_model = unprinted_models.pop()
		print(f"\nPrinting model: {current_model.title()}")
		completed_designs.append(current_model)

def show_completed_models(completed_designs) : 
	print("\nThe commpleted models are: ")
	for completed in completed_models:
		print(completed.title())
    	
remaining = ['phone case', 'robot pendant', 'dodecahedron']
completed = [ ]   
print_models(remaining,completed) 
show_completed_models(completed)

#Excercise

"""
Messages:Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
"""
def show(messages):
	print("\nThe messages are: ")
	for message in messages: 
		print(message.title())

msgs = ['hello','i am kinda busy',"i'll talk to you later"]	
show(msgs)
print('')	

"""
Sending Messages:With the copy of the above funcion. Write a funtion called send_messags() that prints each message and moves it to a new list
called sent_messages(). After calling the function , print the both of your lists to make sure that the messages were moved correctly
"""

def send_messages(unsent_messages,sent_messages):
	while unsent_messages:
		current_message = unsent_messages.pop()
		print(f"Sending message : {current_message.title()}")
		sent_messages.append(current_message)

def show_messages(unsent_messages,sent_messages):
    print(f"\nThe unsent messages are: {unsent_messages}")
    print(f"\nThe sent messages are: {sent_messages}")		

sent_msgs = []
send_messages(msgs,sent_msgs)
show_messages(msgs,sent_msgs)


"""
Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
unsent = ['good morning', 'have a good day']
sent = []
send_messages(unsent[:],sent)
show_messages(unsent,sent)

#we passsed a copy of the list to the function so that he original remains the same without being changedcd

        	


