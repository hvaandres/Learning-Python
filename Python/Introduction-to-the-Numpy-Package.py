# You will need to install numpy on your operative system.

"""
1.- If you have python 3, you will need to type pip3 install numpy.

observation: You can install an upgrade version of pip. To do this, you will need to type "pip install -U pip" If this command doesn't work it's because you have python 3 installed which you will need to type pip3 install -U pip.

windows = python -m pip install -U pip


"""



import numpy as np

num_range = np.arange(16)

num_range

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

num_range.reshape(4, 4)

# array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])