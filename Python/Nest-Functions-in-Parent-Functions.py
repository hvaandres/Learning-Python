
# Nested Functions
# Greeting = will contain two values
# Full_Name = will contain the same values. This way allow us to have a more compaling and clean code....

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')

greeting ('andres', 'haro')