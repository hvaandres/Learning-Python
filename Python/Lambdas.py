# Python allows you to create anonymous function i.e function having no names using a facility called lambda function. lambda functions are small functions usually not more than a line.

full_name = lambda first, last: f'{first} {last}'

def greeting(name):
  print(f'Hi there {name}')

greeting(full_name ('Andres', 'Haro') )