#For loop is used when we know the exact no of times we want to run the loop. It iterates over a sequence such as list, tuple or range 
#In contrase, while loop is used when we want to repeat a block of code as long as a certain condition is true..
#A for loop
for i in range(1,5,2):
	print(i)
print("")	

#A while loop
count_number = 0
while count_number < 5:
	print(count_number)
	count_number += 1

#A game: Letting the user choose when to quit
"""
prompt = "Tell me something, and I will repeat it back to you.."
prompt += "\nEnter quit to end the game: "	
message =''
while message != 'quit':
	message = input(prompt)
	print(message)
	"""

#Above code works well, except that it prints the word "quit" as if it were an actual message
#A simple if test fixes this:
prompt = "Tell me something, and I will repeat it back to you.."
prompt += "\nEnter quit to end the game: "
message = ''
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)	

"""We can solve the above issue by also using this
prompt = "Tell me something ,I'll repeat it back to you until and unless you enter 'quit' " 
message = input(prompt)
while message != 'quit': 
	print(message)
	message = input(prompt)
	"""


#Using a flag
#A flag is a boolean value that is used to signal or indicate that the certain condition has been met
#We can write our programs so they run while the flag is set true and stop running when any of the several events set the flag value to False
prompt = "Tell me something, and I will repeat it back to you.."
prompt += "\nEnter quit to end the game: "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
	    print(message)	
	    
#Using a break to exit a loop




 





	



