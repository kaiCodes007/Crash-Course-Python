#Importing an entire module:
#The general syntax is : module_name.function_name()

import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushroom','green peppers','extra cheese')


#Using 'as' to Give a module an alias:

import pizza as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'olive','pineapple','mushroom')
