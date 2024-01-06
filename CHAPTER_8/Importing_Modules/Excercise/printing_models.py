#Entire module
#import printing_functions
#Or the equivalent:with an alias
import printing_functions as pf

remaining = ['phone case','robot pendant','dodecahedron']
completed = []

pf.printing_designs(remaining, completed)
pf.show_printed_designs(completed)

print('')

#Importing a specific function
#from printing_functions import printing_designs, show_printed_designs 
#A better approach would be:
from printing_functions import printing_designs as pd, show_printed_designs as spd

remaining = ['jwellery', 'figurines', 'sculpture']
completed = [] 

pd(remaining, completed)
spd(completed)

#Importing all functions
from printing_functions import *

