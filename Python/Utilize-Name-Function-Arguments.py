def full_name(first, last):
  print(f'{first}{last}')

#All of this named arguments will work to mantain order in your callable

full_name('andres', ' haro')
full_name(first = 'andres', last = ' haro')
full_name(last = ' haro', first = 'andres')