#Solving 'Try It Yourself' problems
"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create 
an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it 
again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number 
and print the value again.Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
"""

class Restaurant:
	def __init__(self,restaurant_name,cuisine_name):
		self.name = restaurant_name
		self.cuisine = cuisine_name
		self.number_served = 0

	def restaurant_description(self):
		print(f"The name of the restaurant is {self.name.title()}")
		print(f"This restaurant serves {self.cuisine.title()} food\n")

	def served_customers_number(self):
		#Displaying the number of served customers.
		
		print(f"The total served customers are: {self.number_served}")

	def set_number_served(self,number):
		#Writing a method that allows to set the number of of the new no of total served customers
	   
	   if number >= self.number_served:
	       self.number_served = number

	   else :
	   	    print("You cant roll down the served number served")

	
	def increment_number_served(self,no):
		#Writing a fucntion that allows to add the new no of served customers to the existing value 
		self.number_served += no


my_restaurant = Restaurant('Kai Restaurant','Italian')

#Displaying restaurant details:
my_restaurant.restaurant_description()

#Displaying the original default value
my_restaurant.served_customers_number()	

#Changing the served numbers directly through instance and displaying it again
my_restaurant.number_served = 100
my_restaurant.served_customers_number()

#With the set_number_served() method
my_restaurant.set_number_served(240)
my_restaurant.served_customers_number()

#With the increment_number_served() method
my_restaurant.increment_number_served(360)
my_restaurant.served_customers_number()


"""
Login Attempts: Add an attribute called login_attempts to your User class from Ex. 9-3(page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts
to 0.Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it 
was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

"""

class User:
	def __init__(self,first,last,address):
		self.first = first
		self.last = last
		self.address = address
		self.login_attempts = 1

	def greet_user(self):
	    print(f"Hello, {self.first.title()} {self.last.title()}\n")	

	def describe_user(self):
		print(f"The full name of the user is : {self.first.title()} {self.last.title()}")
		print(f"The user lives in {self.address.title()} ")
		print(f"The login attempts of the user is : {self.login_attempts}\n")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

#Creating an instance
kai = User('bill', 'bryson', 'nashhville')

#Greeting the user with greet_user() method
kai.greet_user()

#Displaying all information about the user using describe_user() method
kai.describe_user()

#Calling the increment_login_attempts() method several times
print("Trying to log in:")
kai.increment_login_attempts()
kai.increment_login_attempts()
kai.increment_login_attempts()
kai.increment_login_attempts()
print(f"The total no of login attempts is : {kai.login_attempts}\n")

#Resetting the login attempts to 0 and displaying it for conformation
kai.reset_login_attempts()
print(f"The total no of login attempts has been set to {kai.login_attempts}\n")


print("Keep your chin up ,man... You are doing great.. ")
