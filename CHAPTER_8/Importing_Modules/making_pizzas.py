#1.Importing an entire module:
#The general syntax is : import module_name

import pizza
#When calling a function : module_name.function_name()
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushroom','green peppers','extra cheese')

#Using 'as' to Give a module an Alias:
#The general syntax is: import module_name as mn

import pizza as p
#When calling a function: alias_name.function_name()
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'olive','pineapple','mushroom')



#2.Importing a specific function from a module
#The general syntax: from module_name import function_name
#For multiple functions: from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(12,'green peppers')
make_pizza(14,'french fries','extra cheese','pepperoni')

#Using 'as' to give function an Alias
from pizza import make_pizza as mp

mp(16,'sausage')
mp(12,'ham','spinach','shrimp')


#3.Importing all functions from a module
#The general syntax is : from module_name import *

from pizza import *

make_pizza(16,'bacon')
make_pizza(12,'chicken','tomatoes','tuna')



