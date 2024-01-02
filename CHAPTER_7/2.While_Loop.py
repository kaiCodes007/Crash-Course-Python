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
"""An example of break statement with while loop

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
In this example, the while loop prints the current value of count in each iteration. However,
when count becomes equal to 3, the break statement is encountered, and the loop is immediately terminated.
In Python, the break statement is used to exit or terminate a loop prematurely, before the normal loop condition is met
"""

prompt = "Please enter the city you have visited"
prompt += "\nEnter exit to stop: "

while True:
	city = input(prompt)
	if city == "exit":  
		break
	else : 
	    print(f"I'd love to go to {city.title()}\n")
#It is used to exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test.    

#Using continue in a loop
"""Rather than breaking out of a program entirely without executing the rest of the code..we can use continue statement to return to the beginning 
of the loop based on the result of a conditional test
The code below ignores the print statement when it enocunters i==2,rather than breaking out of it unlike break
for i in range(5):
	if i == 2:
		continue
	print(f"{i}\n")	
	"""


#A program that counts from 1 to 10 but prints only the even number
current_number = 0
print("The odd numbers are: ") 
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
		print("I dare you to print this line")	
	else:
	    print(current_number)

	    	






 





	



