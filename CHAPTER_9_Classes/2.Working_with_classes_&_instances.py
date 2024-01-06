#Lets define a Car class that neatly takes three parameters make,model and year along with the self
"""
class Car:
	def __init__(self,make,model,year):
		#Intialize the attributes
		self.make = make
		self.model = model 
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.year} {self.model}"
		return long_name

my_new_car = Car('audi','a4',2019)	
print(my_new_car.get_descriptive_name())
"""


#To make it more interesting lets add an attribute that changes over time. We'll add an attribute that stores the car's overall mileage

#Setting a default value for an Attribute:	
#Lets copy the above code: and ad

class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self): 
	    print(f"This car has {self.odometer_reading} miles left on it.")	

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


#Clearly, not many cars are sold with exactly 0 miles on the odometer so.We need a way to change the value of the attribute

#Modifying attribute values

#modifying an attribute directly through an instance

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Modifying an attribute's value through a Method(by making a function inside the class)
class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 50


	def read_odometer(self): 
	    print(f"This car has {self.odometer_reading} miles left on it.")

	def update_odometer(self,mileage):
		"""
		Taking in a value for mileage and assigning it to self.odometer_reading
		
		self.odometer_reading = mileage
		"""
		
		#Or we can add some more logic
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
		    print("\nYou cant roll back an odometer")	

my_new_car = Car('audi','a4',2019)
my_new_car.update_odometer(46)
my_new_car.read_odometer()


#Incrementing an attribute's value through a method. Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it.

class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
	    full_name = f"\n{self.year} {self.make} {self.model}"	
	    return full_name.title()

	def update_odometer(self, mileage):
	    if mileage >= self.odometer_reading:
	        self.odometer_reading = mileage
	    else:
	        print("You cant roll back an odometer")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles left on it")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())		

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



