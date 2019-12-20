# we need to understand the difference in between input and output
# Also we need to know the difference in between print and return. print: will print information. return: will return a value that has been stored in somewhere

def full_name(first, last):
  return f'{first} {last}'

# Stored the function inside of a variable
# In this way, you will be able to call that variable at anytime.

Haro = full_name('Andres', 'Haro')

def greeting(name):
  print(f'Hi {name}!')


greeting(Haro)