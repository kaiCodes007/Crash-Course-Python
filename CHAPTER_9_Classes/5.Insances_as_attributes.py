class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year

	def car_detail(self):
		model_detail = f"\n{self.year} {self.make} {self.model}"
		return model_detail.title()


class Battery: 
	def __init__(self, battery_size = 75):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has {self.battery_size}-kWh battery")	


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

		self.battery = Battery(100)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.car_detail())

my_tesla.battery.describe_battery()


#Lets carry out an another example::

class Bike:	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year

	def bike_description(self):
	    bike_detail = f"{self.year} {self.make} {self.model}"
	    return bike_detail.title()	

class Battery: 
	def __init__(self, battery_size): 
	    self.battery_size = battery_size

	def describe_battery(self):
		print(f"This bike has {self.battery_size}-kwh battery")

	def get_range(self):
	    if self.battery_size == 75 :
	        range = 250
	    elif self.battery_size == 100:
	        range = 315
	    print(f"This bike can go up to {range} in one charge")    

class ElectricBike(Bike):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery(75)


my_bike = ElectricBike('XYZ', 'E-Mountain', 2022)
print(my_bike.bike_description())
my_bike.battery.get_range()		




