def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {''.join(args)}, I hope you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')

greeting('Morning',
        'Andres', 'Haro',
        first = 'Clean your room',
        second = 'Be ready for work',
        third = 'Homework from the coding bootcamp')