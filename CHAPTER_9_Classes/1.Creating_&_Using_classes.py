"""
Lets create a class named Dog, that represents a dog, not one dog in particular,but any dog . What do we know about dogs? 
Well, they have a name and an age. And they do sit and roll over. Those two piece of information (name and age) and those 
two behaviors(sit and roll over) will go to class Dog because they're common to most dogs
"""

class Dog:

	def __init__(self, name, age):
	   #Initialize name and age attributes
	   self.name = name
	   self.age = age

	def sit(self):
		#Simulate a dog sitting in response to command
		print(f"{self.name.title()} is now sitting.\n ")

	def roll_over(self):
		#Simulate a roll over in resopnse to a commmand
		print(f'{self.name.title()} rolled over\n')

#Making an instance from a class
#Syntax: instance_name = class_name(parameter_0, parameter_1)

my_dog = Dog("tiger", 12)

#Accessing attributes
#Syntax: instance_name.attribute_name

print(f"My dog's name is {my_dog.name.title()}\n")
print(f"My dog's age is {my_dog.age}\n")

#Here, my_dog.name looks at the instance my_dog and find the attribute 'name' associated with my_dog. This is the same attribute referred to as self.nam in class Dog
#And the same goes with my_dog.age


#Calling Methods
#syntax: instance_name.method_name()
#Lets make my dog sit and roll over
my_dog.sit()
my_dog.roll_over()



#Creating multiple instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()


print(f"Your dog's name is {your_dog.name.title()}")
print(f"Your dog's age is {your_dog.age}")
your_dog.roll_over()



#Solving 'Try It Yourself' problems
"""
Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a 
message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, 
and then call both methods.
"""
#Defining a class
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type


	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.name.title()}")
		print(f"It offers {self.cuisine.title()} food\n")

	def open_restaurant(self):
		print(f"{self.name.title()} is Open\n")

#Creating an instance from the above class
restaurant = Restaurant('atithi cafe and restro', 'italian')

#Calling methods
restaurant.describe_restaurant()

restaurant.open_restaurant()

"""
Three Restaurants: Start with your class from above excercise. Create three different instances from the class, and call 
describe_restaurant() for each instance.
"""
#Creating three different instances for the above 

my_restaurant = Restaurant('burger bouse','chinese')
your_restaurant = Restaurant('kfc', 'american')
his_restaurant = Restaurant('macdonalds', 'english')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()


"""
Printing them wtih more description:

print(f"My restaurant's name is : {my_restaurant.name.title()}")
print(f"My restaurant offers {my_restaurant.cuisine.title()} food\n")

print(f"Your restaurant's name is : {your_restaurant.name.title()}")
print(f"Your restaurant offers {your_restaurant.cuisine.title()} food\n")

print(f"His restaurant's name is : {his_restaurant.name.title()}")
print(f"His restaurant offers {his_restaurant.cuisine.title()} food\n")
"""


"""
Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user()
that prints a personalized greeting to the user. Create several instances representing different users, and call both methods
for each user.
"""

class User:
	def __init__(self,first_name,last_name,address,hobby):
		self.first = first_name
		self.last = last_name
		self.address = address
		self.hobby = hobby

	def describe_user(self):
		full_name = f"{self.first} {self.last}"
		print(f"The fullname of user is : {full_name.title()}")
		print(f"The user lives in {self.address.title()} ")
		print(f"The user enjoys {self.hobby.title()}\n")

	def greet_user(self)	:
		print(f"Hello, {self.first.title()} {self.last.title()}\n")


kai = User('asmit','chhetri','kathmandu','playing soccer')
kai.greet_user()
kai.describe_user()		




	    		

