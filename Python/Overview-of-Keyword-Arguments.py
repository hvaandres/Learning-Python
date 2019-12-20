def greeting (**kwargs):
  print(kwargs)

greeting()
greeting(first = 'Andres', last ='Haro')

def greeting (**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest')

greeting()
greeting(first = 'Andres', last = 'Haro')