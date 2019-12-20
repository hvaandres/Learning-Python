def greeting(*args):
  print('Hi ' + ''.join(args))

greeting('Andres ', 'A', 'Haro')
greeting('Lizbeth ', 'Haro')


# We can run this as well but it would be more recommend it if we use the words args (arguments)

def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')

# Traditional and positional argument
# We can add the day and more text 

def greeting(time_of_day, *args):
  print(f"Hi {''.join(args)}, I hope that you're having a good {time_of_day}")
greeting('Afternoon', 'Alan ', 'A ', 'Haro')
greeting('Morning ', 'Aldo ', 'Haro')  