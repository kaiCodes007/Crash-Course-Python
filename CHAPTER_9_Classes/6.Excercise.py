"""
An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise
9-1(page 162) or Exercise 9-4(page 167).Either version of the class will work; just pick the one you like better. Add an attribute called flavors
that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
	def __init__(self, restaurant_name, cuisine_name):
		self.name = restaurant_name
		self.cuisine = cuisine_name

	def describe_restaurant(self):
		detail = f"The name of the restaurant is : {self.name.title()}. It serves best {self.cuisine.title()} "
		return detail

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, ):
    	super().__init__(name,cuisine)
    	self.flavors = ['vanilla', 'strwberry', 'pineapple']

    def display_flavors(self):
    	print("The flavor this stand serves are: ")
    	for flavor in self.flavors:
            print(f'- {flavor}')
        	

my_icecream_stand = IceCreamStand('Kai icecream stand', 'Ice-Cream')
print(my_icecream_stand.describe_restaurant()) 
my_icecream_stand.display_flavors()
print('')

"""
Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3(page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and 
so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
"""

class User:
	def __init__(self, first, last, address):
		self.first = first
		self.last = last
		self.address = address

	def describe_user(self):
	    print(f"The user's full name is : {self.first.title()} {self.last.title()}")
	    print(f"The user's address is : {self.address.title()}")

class Admin(User):
	def __init__(self, first = 'admin', last = " " , address = " "):  #pov: admin doesnt show his details 
		super().__init__(first, last, address)
		self.privileges = ['can add post', 'can delete post','can ban user']

	def show_privileges(self):
		print("The privileges this user has, are: ")
		for privilege in self.privileges:
			print(f"- {privilege.title()}")

server_admin = Admin('Kai',"chhetri","kathmandu")
server_admin.describe_user()
server_admin.show_privileges()
print('')


"""
Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in 
Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
"""
class User:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def describe_user(self):
	    print(f"The user's full name is {self.first.title()} {self.last.title()}")	

class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(f"The privileges are: ")
		for privilege in self.privileges:
			print(f"- {privilege}")

class Admin(User):
	def __init__(self, first = "admin", last = " "):
		super().__init__(first, last)
		self.rights = Privileges(['can add post','can delete post','can ban user'])

site_admin = Admin()
site_admin.describe_user()
site_admin.rights.show_privileges()		

