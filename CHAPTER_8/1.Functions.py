#Function Definition
def greet_me():
	#Display a simple greeting
	print("Hello, Have a good day\n")

#Function Call
greet_me()
#As the function requires no additional information to work... Its parentheses are kept empty

#Passing information to a function 
def greet_user(username):
	#The variable username is an example of parameter
	print(f"Hello,{username.title()}\n")

greet_user('Kai')
#The value Kai, inside the parentheses is an example of argument.
#Entering greet_user('Kai') calls greet_user() and gives the function the information it needs to execute print() call

#A parameter is a variable that is used in the function definition, which serves as the placeholder for the actual value that will be passed during the function call
#An argument is a value that's passed to the parameter when the function is called

#Excercise: 
#Write a function called display_message() that prints one sentence telling what you are learning about. Call the function. 

def display_message():
	print("Hello cosmos, I am learning about Python functions\n")
display_message()


#Write a function called favorite_book that accepts one parameter,title. Make the function print a message

def favorite_book(title):
    print(f"One of my favorite book is {title.title()}\n")

favorite_book("crash course python")


#Passing arguments
#Positional arguments:values passed to a function in the order in which the parameters are defined in the function signature.

def describe_pet(animal_type,pet_name):
	print(f"I have a {animal_type.title()} named {pet_name.title()}\n")
describe_pet('dog','tiger')	

#Multiple function calls
describe_pet('hamstring','harry')
describe_pet('cat','marco')
#Note that the order matters in positional arguments


#Keyword Arguments: A name-value pair passed to the function
describe_pet(animal_type = 'rat', pet_name = 'chuck')
describe_pet(pet_name = 'chuck', animal_type = 'rat')
#The above two function calls are equivalent. The keyword arguments free you from the nuisance of remembering the correct order of the arguments


#Default values
def describe_pet(pet_name,animal_type = 'dog') :
    print(f"I have a {animal_type.title()} named {pet_name.title()}\n")
describe_pet('willie')
#Note that the order of the parameters had to be changed as python still interprets this a positional argument

#Equivalent function calls: As positional arguments, keyword arguments and default values can all be used together , there are several ways to call a function
"""
describe_pet('harry','hamstring') 
describe_pet(pet_name = 'harry', animal_type = 'hamstring')
describe_pet(animal_type = 'hamstring', pet_name = 'harry')  

All three of those above function calls are equivalent in terms of the most latter one funcion defined.
"""

#Excercise
"""A function named make_shirt that accepts a size and text of a message that should be printed on the shirt. Print a sentence with the summary
Call the function using positional argument and keyword argument
"""
def make_shirt(size,message):
	print(f"I want a shirt, written '{message.title()}' on size {size.upper()}\n")
#Positional argument
make_shirt('xl','python is fun')
#Keyword argument
make_shirt(message = 'Coding is awesome', size = 'L')


"""Modify the make_shirt() so that the shirts are large by default with a message that reads 'I love python'
Make a large shirt and a medium shirt with the default message and a shirt of any size with a different messafe
"""
def make_shirt(size = 'Large', message = 'i love python'):
	print(f"I want a shirt, written '{message.title()}' on size {size.title()}")
#A large shirt with default message value
make_shirt()

#A medium shirt with default message
make_shirt('medium')

#A shirt of any size with a different message
make_shirt('anysize',"I am super-cool")

#Equivalent function call for the last one
make_shirt(size = 'anysize', message = 'I am super-cool')
make_shirt(message = 'I am super-cool', size = 'anysize')


"""Write a function called describe_city() that accepts the name of a city and its country. Give the parameter for the country a default value
.Print a simple sentence , such as Kathmandu is in Nepal for three different cities , at least one of which is not default country
"""	
def describe_city(city,country = 'nepal'):
	print(f"\n{city.title()} lies in {country.title()}")
describe_city('kathmandu')
describe_city(city = 'pokhara')	
describe_city('delhi','india')