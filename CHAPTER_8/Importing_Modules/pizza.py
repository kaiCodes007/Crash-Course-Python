#Creating pizza module

def make_pizza(size,*toppings):
	print(f"\nMaking a {size}-inch pizza with following requested toppings: ")
	for topping in toppings:
		print(f"- {topping.title()}")

