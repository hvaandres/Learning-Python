# The easiest way is to do the following:

#Open your Terminal

from math import sqrt

sqrt(4)

# This file should be named as Alan
# Then go back to the Terminal
#Type the following:

import sys
sys.path.insert(0, './libs')
from helper import greeting

def render():
    print(greeting('Alan', 'Haro'))
render()


# How to Import a Module and Assign an Alias in Python

import sys
sys.path.insert(0, './libs')
import helper as aa

def render():
    print(aa.greeting('Tiffany', 'Hudgens'))


render()


import math as m

m.sqrt(4)