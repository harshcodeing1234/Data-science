# How importing in python works
import math

result = math.sqrt(9)
print(result)  


# from keyword
from math import sqrt

result = sqrt(64)
print(result) 

# 
from math import sqrt, pi

result = sqrt(9)
print(result)  
print(2*pi) 


# importing everything
from math import *

result = sqrt(6789)
print(result)  
print(pi)  


# The "as" keyword
import math as m

result = m.sqrt(9)
print(result)  
print(m.pi)  


# The dir function:  use to view the names of all the functions and variables defined in a module. 
import math

print(dir(math))
print()

# Create a module myself
from harsh import welcome,harsh
welcome()
print(harsh)

import harsh
harsh.welcome()
print(harsh.harsh)

from harsh import *
welcome()
print(harsh)