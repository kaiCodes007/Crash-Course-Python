#Passing an arbitrary number of arguments:When a function does not know the number of arguments it needs to accept ahead of time
def make_pizza(*toppings):
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

#Summarizing the pizza being ordered using for loop(I am making a new function for my own practice. If you intend on keeping a good memory of what you had done, repetition will pay in good manner for sure)

def bake_pizza(*toppings):
	print("\nMaking a pizza with following toppings: ")
	for topping in toppings:
		print(f"- {topping.title()}")

bake_pizza('pineapple')	
bake_pizza('olive','french fries','mushroom')	


#Mixing Positional and Arbitrary Arguments:If a function needs to accept several different kinds of arguments, the parameter that accepts the arbitrary no. of arguments must be placed last in the function definition
def prepare_pizza(size,*toppings):
	print(f"\nMaking a {size}-inch pizza with following toppings: ")
	for topping in toppings:
		print(f"- {topping.title()}")

prepare_pizza(16, 'green pepper')
prepare_pizza(12,'olive','mushroom','extra cheese')	


#Using Arbitrary Keyword Arguments:When we want a function to take an arbitrary no of arguments but not sure about the type of information that will be passed to the function
def build_profile(first,last,**user_info):
	"""Build a dictionary containng all the information we know about the user"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')	
print(f"\n{user_profile}\n")


#Excercise
"""
Sandwiches: Write a function that accepts a list of items a person wants on sandwich . The function should have one parameter that collects as many 
items as the function call provides, and it should print a summary of the sandwich that's being ordered. Call the function three times
,using a different number of arguments each time.(hint:Use arbitrary number of arguments)
"""
def make_sandwich(*fillings):
	print("\nPreparing sandwich with following requested fillings: ")
	for filling in fillings:
		print(f"- {filling.title()}")

make_sandwich('ham')
make_sandwich('chicken','provolone')
make_sandwich('roast beef','swiss','lettuce','tomato')	


"""
User Profile: Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that
describe you.(Hint:Use Arbitrary Keyword Arguments)
"""	
def build_profile(first,last,**my_info):
	#Packing the expected info about myself to my_info dictionary
	my_info['first_name'] = first
	my_info['last_name'] = last
	return my_info

my_profile = build_profile('lionel','messi',address = 'rosario',nationality = 'argentina', field = 'football')	
print(f"\n{my_profile}")

"""
Cars:Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments.Call the function with two other key-value pairs along with the required information
"""

def make_car(manufacturer_name,model_name,**car_info):
	car_info['manufacturer'] = manufacturer_name
	car_info['model'] = model_name
	return car_info

car = make_car('subaru','outback', color= 'blue', tow_package = True)
print(f"\n{car}")

	

		



