#Lets start with making a Car class as in our previous examples

class Car:
	def __init__(self, make, model, year):
		"""Initializaing the car attributes"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 10

	def get_descriptive_name(self):
	    descriptive_name = f"{self.year} {self.make} {self.model}\n"
	    return descriptive_name.title()	

	def read_odometer(self):
	    print(f"This car has {self.odometer_reading} miles left on it") 

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cant roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

	def fill_gas_tank(self, quantity_in_litres):
		print(f"Just filled {quantity_in_litres} of gas")


#Now creating a child calss ElectricCar:
class ElectricCar(Car):

	def __init__(self, make, model, year):
		"""Initializa the attributes of the parent class"""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.update_odometer(400)
my_tesla.read_odometer()


#Defining Attributes and Methods for the Child class, Overriding methods from the parent class

#As we already have the parent class Car, we are just overriding child class ElectricCar and adding a new attribute battery_size

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 75

	
	def describe_battery(self):
	    print(f"This car has {self.battery_size}-kwh battery\n")

	#Overriding a metod from a parent class
	#As electric cars donot require gas, lets override the fill_gas_tank() method from the parent class
	def fill_gas_tank(self):
		print("Elctric Cars Dont need gas to run")


your_tesla = ElectricCar('tesla', 'model s', 2019) 
your_tesla.increment_odometer(100)
your_tesla.read_odometer()
your_tesla.describe_battery()
your_tesla.fill_gas_tank() 






