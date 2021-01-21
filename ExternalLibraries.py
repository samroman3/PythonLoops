import math

 

#math is a module. A module is just a collection of variables (a namespace, 
# if you like) defined by someone else. Similar to frameworks in swift


print(type(math))

#to see all names in math
print(dir(math))

"""['__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 
'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 
'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']"""

#access using dot syntax eg. math.pi 

print("pi to 4 significant digits = {:.4}".format(math.pi))

#returns the logarithm of x to the given base
math.log(32,2)

# call on >>>help(math) for full list of module methods

#you can also import under mt to save time
# >>>import math as mt
# >>>mt.pi

"Common convention to import numpy as np and import pandas as pd"
# >>>import numpy as np
# >>>import pandas as pd 

"""The math and numpy modules both have functions called log, 
 but they have different semantics. So in these cases we import only what we need from each module"""

#>>>from math import log, pi
#>>>from numpy import asarray

import numpy  

# modules contain variables which can refer to functions or values. Something to be aware of is that 
# they can also have variables referring to other modules

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

#lets roll 10 dice
rolls = numpy.random.randint(low=1 ,high=6, size= 10) 
print(rolls)

#>>>pandas functions will give you DataFrames and Series.
#the graphing library >>>matplotlib has Subplots, Figures, TickMarks, and Annotations.

#back to dice
print(rolls.mean())
#returns the mean of randomly rolled dice

#since numpy uses >>>type(ndarray) we can convert it to typelist using .tolist

print(rolls.tolist)

"""With ndarrays native python operators work differently"""

print(rolls + 10)

#this adds 10 to each element in ndarray
#eg. array([13,11,12,11,11,13,11,15,11,11])

rolls <= 3

#this converts elements in array to a boolean given the operators condition 
# array([ True,  True,  True,  True,  True,  True,  True, False,  True,
#         True])

xlist = [[1,2,3],[4,5,6],]
#create a 2d array
x = numpy.asarray(xlist)

print("xlist = {}\nx = \n{}".format(xlist, x))

# Get the last element of the second row of our numpy array
print(x[1,-1])

"""numpy's ndarray type is specialized for working with 
multi-dimensional data, so it defines its own logic for indexing, 
allowing us to index by a tuple to specify the index at each dimension. 
Unlike lists whitch do not allow indices as tuples"""


# tensorflow, a Python library popularly used for deep learning. 
# makes extensive use of operator overloading (the behavior desrcibing how ndarray interacts with operators).

import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
print(a + b)

