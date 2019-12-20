#Important info:

"""
* - matches everything

? - matches any single character

[seq] - matches any character in seq

[!seq] - matches any character not in seq

"""

import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file, "\b")

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()

Brands = [
    "Ford Fusion FS",
    "Toyota Corolla CR",
    "Volkkswagen Jetta JT",
    "Ferrari Enzo JT"
]

sport_cars = [car for car in Brands if fnmatchcase(car, "* JT")]

print(sport_cars)
