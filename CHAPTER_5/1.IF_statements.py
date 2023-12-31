#Conditional if statements continued
#A revision of if statement
cars=['bmw','suzuki']
for car in cars:
	if car=='bmw':
		print(car.title())
	else:
		print(car.upper())
		print("")	    	

#A conditional if can be single if statement, a if-else statement for two different outcomes
#And an nested elif chain where we can test multiple conditions... in this type of statement 'else'	statement can be avoided

age=21
if age<4:
	print("Your admission cost is $4 only")    
elif age<15:
	print("Your admission cost is $10 only")    
elif age<=21:
	print("Your admission cost is $20")
	print('')
"""
else:
    print('You are not eligible for admission')
    """        
#Testing wheather a value is in list
foods=['pizza','momo','sausage']  
fav_food='thukpa'  
if fav_food in foods:
	print("Your fav_food is in menu\n")
else:
	print("your fav_food is not in list\n")	

#Testing multiple conditions:
requested_toppings=['mushrooms','extra cheese']    
if 'mushrooms' in requested_toppings:
	print("Addinng mushrooms")
	if 'pepperoni' in requested_toppings:
		print("Adding pepperoni")
		if 'extra cheese' in requested_toppings:
			print("Adding extra cheese")
			print("Your pizza is ready\n")


#Excercise: an alien shooting game
alien_color='red'
if alien_color=='red':
	print("Congratulations, you just earned 5 points")
#Another version
if alien_color=='green'	:
	print("Congratulations , you just earned 10 points")
else:
	print("Congratulations you earned 5 points again")	

#else if
alien_color='green'
if alien_color=='green':
	print("You earned 5 points for shooting the alien\n")
else:
	print("There are no points for shooting this alien\n.Thank you.")	

#Unequality test
alien_color='red'
if alien_color !='green':
	print("Congrats, you earned 10 points\n")


#Stages of life : if-elif-else chain
age=40
if age<2:
	print("Baby")
elif age==2 or age<4:
	print("toddler")	
elif age==4 or age<13:
	print("kid")    
elif age==13 or age<20:
	print("teenager")   
elif age==20 or age<65:
	print("adult")     
else:
	print("elder") 
	print('') 


#Wheather my fav_fruits are in the list or not
fruits=['grape','apple','watermelon']  
fav_fruits=['apple','papaya']
for fav_fruit in fav_fruits:
 	if fav_fruit in fruits:
 		print(f"Your favorite fruit {fav_fruit.upper()} is in the list\n")
 	else:
 		print(f'Your favorite fruit {fav_fruit.upper()} is not in list\n')

#checkinf for special cases with if in list
requested_toppings=['mushrooms','green pepper','extra cheese'] 
for requested_topping in requested_toppings :
	if requested_topping=='green pepper':
		print(f"Sorry .. The {requested_topping.upper()} is out of stock")
	else:
		print(f'Adding {requested_topping}')
		print('Your pizza is ready')


#Checking if the list is not empty
requested_toppings=[] 
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f'Adding {requested_topping}')
		print("Your pizza is ready")  
	else:
		print ("Are you sure that you want a plain pizza")    

#using multiple list:
available_toppings=['mushrooms','olive','green pepper','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping.upper()}\n')
	else:
		print(f'Sorry.We dont have {requested_topping.upper()}\n')
		print("Finished making your pizza\n")

"""
Excercise
Hello admin... make a list of five or more usernames includeing the name'admin
write a code that will print a greeting to each user after they log in using loop
If the username is admin.. print a special greeting ,
otherwise print a generic greeting...
"""
user_names=['kai','cozmix','neb','hema','admin']
for user in user_names:
	if user=='admin':
		print(f'Hello {user.title()}, would you like to see a status report?\n')
	else:
		print(f'Hello {user.title()}, thank you for logging in again.\n')

#No users: add an if test to make sure that the list is not empty
if user_names:
	print(user_names)
else:
	print("We need to find some users")
	print('')      
#We can check by removing all the usernames to make sure that the correct message is printed

#Checking usernames... making sure that the comparison is case insensitive... That is if Manish has been used... manish or any other forms with the same letters cannot be used
current_users=['kai','sandy','rana','samman','bhatte','pawan','Manish'] 
new_users=['samman','bhatte','pawan','puspa','ritesh','manish']
current_users_lower=[user.lower() for user in current_users] 
for new_user in new_users :
	if new_user.lower() in current_users_lower:
		print(f"The user_name {new_user} is already taken\n")
	else:
		print(f'The user_name {new_user} is available\n')	


#Printing ordinal numbers
numbers=[1,2,3,4,5,6,7,8,9]	
for number in numbers:
	if number==1:
		print(f"{number}st")
	elif number==2:
	    print(f"{number}nd")
	elif number==3:
	    print(f'{number}rd')
	else:
	    print(f'{number}th')
print('')



#Another mehod
numbers=[1,2,3,4,5,6,7,8,9]	
for number in numbers:
	if number<=3:
		if number==1:
			print(f"{number}st")
		elif number==2:
		    print(f"{number}nd")
		else :
		    print(f'{number}rd')  
	else:
	    print(f'{number}th')
print('')


	    	      	






